#include "talker.hpp"
#include "listener.hpp"
#include "rclcpp/rclcpp.hpp"
#include "cpu_affinity_utils.hpp"

int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);

    if (!(argc > 1 && std::string(argv[1]).substr(std::string(argv[1]).length() - 5) == ".yaml")) {
        std::cerr << "Please provide a .yaml file with CPU affinity mask.\n";
        return 1;
    }

    std::string yaml_path = argv[1];
    auto thread_affinities = load_thread_affinities(yaml_path);
    
    auto talker = std::make_shared<MinimalPublisher>();
    auto listener = std::make_shared<MinimalSubscriber>();

    rclcpp::executors::MultiThreadedExecutor executor;

    executor.add_node(talker);
    executor.add_node(listener);
    
    std::thread thread1([&executor, &thread_affinities]() { 
        setThreadAffinity(thread_affinities.at("thread1"));
        executor.spin(); 
    });
    
    thread1.join();
    
    rclcpp::shutdown();

    return 0;
}