#include "templnode.hpp"
#include <rclcpp/rclcpp.hpp>
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <cpu_affinity_utils.hpp>
#include "rcutils/logging_macros.h"

void check_executor_type(const std::shared_ptr<rclcpp::Executor>& executor) {
    if (dynamic_cast<rclcpp::executors::SingleThreadedExecutor*>(executor.get())) {
        RCUTILS_LOG_INFO("The executor is SingleThreadedExecutor.");
    } else if (dynamic_cast<rclcpp::executors::MultiThreadedExecutor*>(executor.get())) {
        RCUTILS_LOG_INFO("The executor is MultiThreadedExecutor.");
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

    // auto executor = std::make_shared<rclcpp::executors::MultiThreadedExecutor>();
    std::shared_ptr<rclcpp::Executor> executor;
    auto exec_yaml = config["executors"][0];
    auto exec_type = exec_yaml["type"].as<std::string>();
    auto exec_cpu = exec_yaml["cores"];

    if (exec_type == "single_threaded") {
        executor = std::make_shared<rclcpp::executors::SingleThreadedExecutor>();
    } else if (exec_type == "multi_threaded") {
        executor = std::make_shared<rclcpp::executors::MultiThreadedExecutor>();
    }

    check_executor_type(executor);

    std::vector<std::shared_ptr<TemplNode>> nodes;

    for (int i = 0; i < exec_yaml["nodes"].size(); i++) {
        auto node_yaml = exec_yaml["nodes"][i];
        nodes.push_back(std::make_shared<TemplNode>(
            node_yaml["name"].as<std::string>(),
            node_yaml["subscribe"].as<std::string>(),
            node_yaml["publish"].as<std::string>(),
            node_yaml["payload"].as<std::string>()
        ));
    }

    for (auto& node : nodes) {
        executor->add_node(node);
    }
    
    // Spin the executor in the main thread
    executor->spin();

    std::thread thread1([&executor, &exec_cpu]() { 
        setThreadAffinity(exec_cpu.as<std::vector<int>>());
        executor->spin(); 
    });

    thread1.join();
    rclcpp::shutdown();

    return 0;
}