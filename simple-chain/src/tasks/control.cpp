#include "control.hpp"
#include <chrono>
#include <functional>
#include <string>

using std::placeholders::_1;
using namespace std::chrono_literals;

Control::Control()
: Node("control"), count_(0)
{
    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "destination", 10, std::bind(&Control::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::String>("force", 10);
    timer_ = this->create_wall_timer(
    500ms, std::bind(&Control::timer_callback, this));
}

void Control::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I use destination: '%s'", msg.data.c_str());
}

void Control::timer_callback()
{
    auto message = std_msgs::msg::String();
    message.data = "Force " + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
}