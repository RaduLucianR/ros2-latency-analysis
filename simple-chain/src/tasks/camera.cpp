#include "camera.hpp"
#include <string>

using namespace std::chrono_literals;
using std::placeholders::_1;

Camera::Camera()
: Node("camera"), count_(0)
{
  publisher_ = this->create_publisher<std_msgs::msg::String>("raw_images", 10);
  timer_ = this->create_wall_timer(
  500ms, std::bind(&Camera::timer_callback, this));
}

void Camera::timer_callback()
{
  auto message = std_msgs::msg::String();
  message.data = "Image " + std::to_string(count_++);
  RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  publisher_->publish(message);
}
