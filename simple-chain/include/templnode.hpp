#ifndef TEMPLNODE_HPP
#define TEMPLNODE_HPP

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class TemplNode : public rclcpp::Node
{
public:
    TemplNode(const std::string& name, 
            const std::string& sub_topic, 
            const std::string& pub_topic,
            const std::string& payload
    );

private:
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    std::string msg_size = "128B";

    void topic_callback(const std_msgs::msg::String & msg) const;
    void timer_callback();
};

#endif