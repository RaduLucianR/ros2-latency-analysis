#ifndef MESSAGE_PRESETS_HPP
#define MESSAGE_PRESETS_HPP

#include <string>
#include "std_msgs/msg/String.hpp"

class MessagePresets {
public:
    static std_msgs::msg::String createMessageOfSize(size_t size_in_bytes) {
        std_msgs::msg::String msg;
        msg.data = std::string(size_in_bytes, 'x'); // Fill with 'x' characters or any character you prefer
        return msg;
    }

    static std_msgs::msg::String msg_128B() {
        return createMessageOfSize(128); // 128 bytes
    }

    static std_msgs::msg::String msg_1KB() {
        return createMessageOfSize(1024 * 1); // 1KB
    }

    static std_msgs::msg::String msg_10KB() {
        return createMessageOfSize(1024 * 10); // 10 KB
    }

    static std_msgs::msg::String msg_100KB() {
        return createMessageOfSize(1024 * 100); // 100 KB
    }

    static std_msgs::msg::String msg_500KB() {
        return createMessageOfSize(1024 * 500); // 500 KB
    }
};

#endif
