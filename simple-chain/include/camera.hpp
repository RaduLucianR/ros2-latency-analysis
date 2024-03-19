#ifndef CAMERA_HPP
#define CAMERA_HPP

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Camera : public rclcpp::Node
{
public:
  Camera();

private:
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
  
  void timer_callback();
};

#endif // CAMERA_HPP
