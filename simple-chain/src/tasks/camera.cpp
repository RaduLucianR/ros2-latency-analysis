#include "camera.hpp"
#include <string>
#include "msg_size.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

Camera::Camera()
: Node("camera"), count_(0)
{
  this->declare_parameter<std::string>("message_size", "128B");

  publisher_ = this->create_publisher<std_msgs::msg::String>("raw_images", 10);
  timer_ = this->create_wall_timer(
  500ms, std::bind(&Camera::timer_callback, this));
}

void Camera::timer_callback()
{
  std::string size_param = this->get_parameter("message_size").get_value<std::string>();
  auto message = std_msgs::msg::String();
  auto print_msg = "Image " + std::to_string(count_++);

  message.data = getMsgOfSize(size_param);
  RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", print_msg);
  publisher_->publish(message);
}