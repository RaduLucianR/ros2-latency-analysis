#include "talker.hpp"
#include <string>
#include "msg_size.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

MinimalPublisher::MinimalPublisher() 
: Node("talker"), count_(0)
{
  this->declare_parameter<std::string>("message_size", "128B");

  publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
  timer_ = this->create_wall_timer(
  500ms, std::bind(&MinimalPublisher::timer_callback, this));
}

void MinimalPublisher::timer_callback()
{
  std::string size_param = this->get_parameter("message_size").get_value<std::string>();
  auto message = std_msgs::msg::String();
  auto print_msg = "message " + std::to_string(count_++);

  message = getMsgOfSize(size_param);
  RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", print_msg.c_str());
  publisher_->publish(message);
}