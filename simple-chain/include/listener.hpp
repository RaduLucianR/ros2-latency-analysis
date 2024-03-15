#ifndef LISTENER_HPP
#define LISTENER_HPP

#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber();

  private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

    void topic_callback(const std_msgs::msg::String & msg) const;
};

#endif