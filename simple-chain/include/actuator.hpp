#ifndef ACTUATOR_HPP
#define ACTUATOR_HPP

#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Actuator : public rclcpp::Node
{
public:
  Actuator();

private:
  void topic_callback(const std_msgs::msg::String & msg) const;
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

#endif // ACTUATOR_HPP
