#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class Fusion : public rclcpp::Node
{
  public:
    Fusion()
    : Node("fusion"), count_(0)
    {
      subscription_ = this->create_subscription<std_msgs::msg::String>(
      "raw_images", 10, std::bind(&Fusion::topic_callback, this, _1));

      publisher_ = this->create_publisher<std_msgs::msg::String>("fused_info", 10);
      timer_ = this->create_wall_timer(
      500ms, std::bind(&Fusion::timer_callback, this));
    }

  private:
    void topic_callback(const std_msgs::msg::String & msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I fuse image: '%s'", msg.data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

    void timer_callback()
    {
      auto message = std_msgs::msg::String();
      message.data = "Fused info " + std::to_string(count_++);
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_->publish(message);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Fusion>());
  rclcpp::shutdown();
  return 0;
}