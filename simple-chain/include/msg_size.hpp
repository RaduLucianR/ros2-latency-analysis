#ifndef MESSAGE_PRESETS_HPP
#define MESSAGE_PRESETS_HPP

#include <string>
#include <regex>
#include "std_msgs/msg/string.hpp"

class MessagePresets {
public:
    static std_msgs::msg::String getMsgOfSize(const std::string& size_str) {
        size_t size_in_bytes = parsePayloadSize(size_str);
        std_msgs::msg::String msg;
        msg.data = std::string(size_in_bytes, 'x'); // Fill with 'x' characters or any character you prefer
        return msg;
    }

private:
    static size_t parsePayloadSize(const std::string& size_str) {
        static const std::regex size_regex(R"((\d+)([Kk]?B)?)");
        std::smatch match;
        if (std::regex_match(size_str, match, size_regex)) {
            size_t multiplier = 1;
            if (match[2].str() == "KB" || match[2].str() == "kb") {
                multiplier = 1024;
            }
            return std::stoi(match[1].str()) * multiplier;
        } else {
            // Default to 128 bytes if invalid format
            return 128;
        }
    }
};

#endif
