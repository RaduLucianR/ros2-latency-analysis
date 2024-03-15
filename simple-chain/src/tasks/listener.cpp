#include "listener.hpp"
#include <string>

using std::placeholders::_1;

MinimalSubscriber::MinimalSubscriber()
: Node("listener")
{
  subscription_ = this->create_subscription<std_msgs::msg::String>(
    "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
}

void MinimalSubscriber::topic_callback(const std_msgs::msg::String & msg) const
{
  RCLCPP_INFO(this->get_logger(), "Message received");
}
