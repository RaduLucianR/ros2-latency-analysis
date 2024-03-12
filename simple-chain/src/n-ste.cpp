#include "tasks/camera.cpp"
#include "tasks/fusion.cpp"
#include "tasks/perception.cpp"
#include "tasks/planning.cpp"
#include "tasks/control.cpp"
#include "tasks/actuator.cpp"
#include "rclcpp/rclcpp.hpp"
#include <thread>

int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);
    
    auto cameraNode = std::make_shared<Camera>();
    auto fusionNode = std::make_shared<Fusion>();
    auto perceptionNode = std::make_shared<Perception>();
    auto planningNode = std::make_shared<Planning>();
    auto controlNode = std::make_shared<Control>();
    auto actuatorNode = std::make_shared<Actuator>();

    rclcpp::executors::SingleThreadedExecutor executor_c;
    rclcpp::executors::SingleThreadedExecutor executor_f;
    rclcpp::executors::SingleThreadedExecutor executor_e;
    rclcpp::executors::SingleThreadedExecutor executor_l;
    rclcpp::executors::SingleThreadedExecutor executor_o;
    rclcpp::executors::SingleThreadedExecutor executor_a;

    executor_c.add_node(cameraNode);
    executor_f.add_node(fusionNode);
    executor_e.add_node(perceptionNode);
    executor_l.add_node(planningNode);
    executor_o.add_node(controlNode);
    executor_a.add_node(actuatorNode);

    std::thread thread1([&executor_c]() { executor_c.spin(); });
    std::thread thread2([&executor_f]() { executor_f.spin(); });
    std::thread thread3([&executor_e]() { executor_e.spin(); });
    std::thread thread4([&executor_l]() { executor_l.spin(); });
    std::thread thread5([&executor_o]() { executor_o.spin(); });
    std::thread thread6([&executor_a]() { executor_a.spin(); });

    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();
    thread5.join();
    thread6.join();

    rclcpp::shutdown();

    return 0;
}
