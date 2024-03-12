#include "actuator.hpp"
#include <string>

using std::placeholders::_1;

Actuator::Actuator()
: Node("actuator")
{
  subscription_ = this->create_subscription<std_msgs::msg::String>(
    "force", 10, std::bind(&Actuator::topic_callback, this, _1));
}

void Actuator::topic_callback(const std_msgs::msg::String & msg) const
{
  RCLCPP_INFO(this->get_logger(), "I apply force");
}
