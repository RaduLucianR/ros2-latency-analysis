#include "camera.cpp"
#include "fusion.cpp"
#include "perception.cpp"
#include "planning.cpp"
#include "control.cpp"
#include "actuator.cpp"
#include "rclcpp/rclcpp.hpp"

int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);
    
    auto cameraNode = std::make_shared<Camera>();
    auto fusionNode = std::make_shared<Fusion>();
    auto perceptionNode = std::make_shared<Perception>();
    auto planningNode = std::make_shared<Planning>();
    auto controlNode = std::make_shared<Control>();
    auto actuatorNode = std::make_shared<Actuator>();
    
    rclcpp::executors::MultiThreadedExecutor executor_1;
    rclcpp::executors::MultiThreadedExecutor executor_2;
    rclcpp::executors::MultiThreadedExecutor executor_3;

    executor_1.add_node(cameraNode);
    executor_1.add_node(fusionNode);

    executor_2.add_node(perceptionNode);
    executor_2.add_node(planningNode);

    executor_3.add_node(controlNode);
    executor_3.add_node(actuatorNode);

    std::thread thread1([&executor_1]() { executor_1.spin(); });
    std::thread thread2([&executor_2]() { executor_2.spin(); });
    std::thread thread3([&executor_3]() { executor_3.spin(); });

    thread1.join();
    thread2.join();
    thread3.join();

    rclcpp::shutdown();

    return 0;
}