#include "planning.hpp"
#include "msg_size.hpp"
#include <chrono>
#include <functional>
#include <string>

using std::placeholders::_1;
using namespace std::chrono_literals;

Planning::Planning()
: Node("planning"), count_(0)
{
    this->declare_parameter<std::string>("message_size", "128B");

    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "perceived_objects", 10, std::bind(&Planning::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::String>("destination", 10);
    timer_ = this->create_wall_timer(
    500ms, std::bind(&Planning::timer_callback, this));
}

void Planning::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I use perceived objects");
}

void Planning::timer_callback()
{
    std::string size_param = this->get_parameter("message_size").get_value<std::string>();
    auto message = std_msgs::msg::String();
    auto print_msg = "Destination " + std::to_string(count_++);
    
    message = getMsgOfSize(size_param);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", print_msg);
    publisher_->publish(message);
}