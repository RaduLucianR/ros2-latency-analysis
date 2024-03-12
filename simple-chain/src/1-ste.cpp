#include "tasks/camera.cpp"
#include "tasks/fusion.cpp"
#include "tasks/perception.cpp"
#include "tasks/planning.cpp"
#include "tasks/control.cpp"
#include "tasks/actuator.cpp"
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
    
    rclcpp::executors::SingleThreadedExecutor executor;

    executor.add_node(cameraNode);
    executor.add_node(fusionNode);
    executor.add_node(perceptionNode);
    executor.add_node(planningNode);
    executor.add_node(controlNode);
    executor.add_node(actuatorNode);
    executor.spin();
    rclcpp::shutdown();

    return 0;
}
