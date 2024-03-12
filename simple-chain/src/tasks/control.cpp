#include "control.hpp"
#include <chrono>
#include <functional>
#include <string>
#include "msg_size.hpp"

using std::placeholders::_1;
using namespace std::chrono_literals;

Control::Control()
: Node("control"), count_(0)
{
    this->declare_parameter<std::string>("message_size", "128B");

    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "destination", 10, std::bind(&Control::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::String>("force", 10);
    timer_ = this->create_wall_timer(
    500ms, std::bind(&Control::timer_callback, this));
}

void Control::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I use destination");
}

void Control::timer_callback()
{   
    std::string size_param = this->get_parameter("message_size").get_value<std::string>();
    auto message = std_msgs::msg::String();
    auto print_msg = "Force " + std::to_string(count_++);
    
    message = getMsgOfSize(size_param);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", print_msg);
    publisher_->publish(message);
}