#include "templnode.hpp"
#include "msg_size.hpp"
#include <chrono>
#include <functional>
#include <memory>

using namespace std::chrono_literals;
using std::placeholders::_1;

TemplNode::TemplNode(const std::string& name, 
          const std::string& sub_topic, 
          const std::string& pub_topic,
          const std::string& payload
) : Node(name)
{   
    msg_size = payload;

    if (!(sub_topic == "NONE")) {
        subscription_ = this->create_subscription<std_msgs::msg::String>(
        sub_topic, 10, std::bind(&TemplNode::topic_callback, this, _1));
    }

    if (!(pub_topic == "NONE")) {
        publisher_ = this->create_publisher<std_msgs::msg::String>(pub_topic, 10);
        timer_ = this->create_wall_timer(
        500ms, std::bind(&TemplNode::timer_callback, this));
    }
}

void TemplNode::topic_callback(const std_msgs::msg::String & msg) const
{
    RCLCPP_INFO(this->get_logger(), "I receive message");
}

void TemplNode::timer_callback()
{
    auto message = getMsgOfSize(msg_size);
    RCLCPP_INFO(this->get_logger(), "Publishing message");
    publisher_->publish(message);
}