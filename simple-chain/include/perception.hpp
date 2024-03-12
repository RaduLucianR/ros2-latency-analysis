#ifndef PERCEPTION_HPP
#define PERCEPTION_HPP

#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Perception : public rclcpp::Node
{
public:
    Perception();

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
    
    void topic_callback(const std_msgs::msg::String & msg) const;
    void timer_callback();
};

#endif // PERCEPTION_HPP