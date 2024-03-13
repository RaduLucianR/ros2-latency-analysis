#include "camera.hpp"
#include "fusion.hpp"
#include "perception.hpp"
#include "planning.hpp"
#include "control.hpp"
#include "actuator.hpp"
#include "rclcpp/rclcpp.hpp"
#include "cpu_affinity_utils.hpp"
#include <thread>

int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);
    
    if (!(argc > 1 && std::string(argv[1]).substr(std::string(argv[1]).length() - 5) == ".yaml")) {
        std::cerr << "Please provide a .yaml file with CPU affinity mask.\n";
        return 1;
    }

    std::string yaml_path = argv[1];
    auto thread_affinities = load_thread_affinities(yaml_path);

    auto cameraNode = std::make_shared<Camera>();
    auto fusionNode = std::make_shared<Fusion>();
    auto perceptionNode = std::make_shared<Perception>();
    auto planningNode = std::make_shared<Planning>();
    auto controlNode = std::make_shared<Control>();
    auto actuatorNode = std::make_shared<Actuator>();
    
    rclcpp::executors::MultiThreadedExecutor executor_c;
    rclcpp::executors::MultiThreadedExecutor executor_f;
    rclcpp::executors::MultiThreadedExecutor executor_e;
    rclcpp::executors::MultiThreadedExecutor executor_l;
    rclcpp::executors::MultiThreadedExecutor executor_o;
    rclcpp::executors::MultiThreadedExecutor executor_a;

    executor_c.add_node(cameraNode);
    executor_f.add_node(fusionNode);
    executor_e.add_node(perceptionNode);
    executor_l.add_node(planningNode);
    executor_o.add_node(controlNode);
    executor_a.add_node(actuatorNode);

    std::thread thread1([&executor_c, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread1"));
        executor_c.spin(); 
    });

    std::thread thread2([&executor_f, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread2"));
        executor_f.spin(); 
    });

    std::thread thread3([&executor_e, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread3"));
        executor_e.spin(); 
    });

    std::thread thread4([&executor_l, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread4"));
        executor_l.spin(); 
    });

    std::thread thread5([&executor_o, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread5"));
        executor_o.spin(); 
    });

    std::thread thread6([&executor_a, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread6"));
        executor_a.spin(); 
    });

    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();
    thread5.join();
    thread6.join();

    rclcpp::shutdown();

    return 0;
}
