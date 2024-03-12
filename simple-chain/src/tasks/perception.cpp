#include "perception.hpp"
#include <chrono>
#include <functional>
#include <string>

using std::placeholders::_1;
using namespace std::chrono_literals;

Perception::Perception()
: Node("perception"), count_(0)
{
    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "fused_info", 10, std::bind(&Perception::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::String>("perceived_objects", 10);
    timer_ = this->create_wall_timer(
    500ms, std::bind(&Perception::timer_callback, this));
}

void Perception::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I analyze fused info: '%s'", msg.data.c_str());
}

void Perception::timer_callback()
{
    auto message = std_msgs::msg::String();
    message.data = "Perceived object " + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
}