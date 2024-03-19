#include "templnode.hpp"
#include <rclcpp/rclcpp.hpp>
#include <yaml-cpp/yaml.h>
#include <iostream>

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);

    if (argc <= 1 || std::string(argv[1]).substr(std::string(argv[1]).length() - 5) != ".yaml") {
        std::cerr << "Please provide a .yaml file with the configuration.\n";
        return 1;
    }

    YAML::Node config = YAML::LoadFile(argv[1]);

    // We will use a single executor for simplicity; adjust if necessary for your use case.
    auto executor = std::make_shared<rclcpp::executors::MultiThreadedExecutor>();
    auto exec_yaml = config["executors"][0];

    for (const auto& node_yaml : exec_yaml["nodes"]) {
        auto node = std::make_shared<TemplNode>(
            node_yaml["name"].as<std::string>(),
            node_yaml["subscribe"].as<std::string>(),
            node_yaml["publish"].as<std::string>(),
            node_yaml["payload"].as<std::string>()
        );

        executor->add_node(node);
    }

    // Spin the executor in the main thread
    executor->spin();

    rclcpp::shutdown();
    return 0;
}