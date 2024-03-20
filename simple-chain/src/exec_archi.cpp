#include "templnode.hpp"
#include <rclcpp/rclcpp.hpp>
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <thread>
#include <vector>
#include <tuple>
#include <cpu_affinity_utils.hpp>
#include "rcutils/logging_macros.h"

void check_executor_type(const std::shared_ptr<rclcpp::Executor>& executor, std::string exec_name) {
    if (dynamic_cast<rclcpp::executors::SingleThreadedExecutor*>(executor.get())) {
        RCUTILS_LOG_INFO("The executor %s is SingleThreadedExecutor.", exec_name.c_str());
    } else if (dynamic_cast<rclcpp::executors::MultiThreadedExecutor*>(executor.get())) {
        RCUTILS_LOG_INFO("The executor %s is MultiThreadedExecutor.", exec_name.c_str());
    } else {
        RCUTILS_LOG_INFO("The executor type is unknown or custom.");
    }
}

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);

    if (argc <= 1 || std::string(argv[1]).substr(std::string(argv[1]).length() - 5) != ".yaml") {
        std::cerr << "Please provide a .yaml file with the configuration.\n";
        return 1;
    }

    YAML::Node config = YAML::LoadFile(argv[1]);
    std::vector<std::tuple<std::shared_ptr<rclcpp::Executor>, std::vector<int>, std::vector<std::shared_ptr<TemplNode>>>> executor_info;
    std::vector<std::thread> threads;

    // Loop to create tuples with executor, exec_cores, and nodes
    for (const auto& exec_yaml : config["executors"]) {
        auto exec_type = exec_yaml["type"].as<std::string>();
        auto exec_name = exec_yaml["name"].as<std::string>();
        std::vector<int> exec_cores = exec_yaml["cores"].as<std::vector<int>>();
        std::shared_ptr<rclcpp::Executor> executor;

        if (exec_type == "single_threaded") {
            executor = std::make_shared<rclcpp::executors::SingleThreadedExecutor>();
        } else if (exec_type == "multi_threaded") {
            executor = std::make_shared<rclcpp::executors::MultiThreadedExecutor>();
        } else {
            std::cerr << "Unsupported executor type: " << exec_type << "\n";
            continue;
        }
        
        check_executor_type(executor, exec_name);

        std::vector<std::shared_ptr<TemplNode>> nodes;
        for (const auto& node_yaml : exec_yaml["nodes"]) {
            nodes.push_back(std::make_shared<TemplNode>(
                node_yaml["name"].as<std::string>(),
                node_yaml["subscribe"].as<std::string>(),
                node_yaml["publish"].as<std::string>(),
                node_yaml["payload"].as<std::string>()
            ));
        }

        executor_info.emplace_back(executor, exec_cores, nodes);
    }

    // Loop to add nodes to their respective executor
    for (auto& info : executor_info) {
        for (auto& node : std::get<2>(info)) {
            std::get<0>(info)->add_node(node);
        }
    }

    // Loop to create threads with the exec_cores for each executor
    for (const auto& info : executor_info) {
        threads.emplace_back([executor = std::get<0>(info), exec_cores = std::get<1>(info)]() {
            setThreadAffinity(exec_cores);
            executor->spin();
        });
    }

    // Join all threads
    for (auto& thread : threads) {
        if (thread.joinable()) {
            thread.join();
        }
    }

    rclcpp::shutdown();
    return 0;
}
