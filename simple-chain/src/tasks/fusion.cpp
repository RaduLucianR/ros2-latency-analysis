#include "fusion.hpp"
#include <chrono>
#include <functional>
#include <string>

using std::placeholders::_1;
using namespace std::chrono_literals;

Fusion::Fusion()
: Node("fusion"), count_(0)
{
    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "raw_images", 10, std::bind(&Fusion::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::String>("fused_info", 10);
    timer_ = this->create_wall_timer(
    500ms, std::bind(&Fusion::timer_callback, this));
}

void Fusion::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I fuse image: '%s'", msg.data.c_str());
}

void Fusion::timer_callback()
{
    auto message = std_msgs::msg::String();
    message.data = "Fused info " + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
}