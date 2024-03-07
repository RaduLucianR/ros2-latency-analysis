cmake_minimum_required(VERSION 3.8)
project(simple-chain)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(camera src/camera.cpp)
ament_target_dependencies(camera rclcpp std_msgs)
add_executable(fusion src/fusion.cpp)
ament_target_dependencies(fusion rclcpp std_msgs)
add_executable(perception src/perception.cpp)
ament_target_dependencies(perception rclcpp std_msgs)
add_executable(planning src/planning.cpp)
ament_target_dependencies(planning rclcpp std_msgs)
add_executable(control src/control.cpp)
ament_target_dependencies(control rclcpp std_msgs)
add_executable(actuator src/actuator.cpp)
ament_target_dependencies(actuator rclcpp std_msgs)
add_executable(camera_fusion src/camera_fusion.cpp)
ament_target_dependencies(camera_fusion rclcpp std_msgs)

install(TARGETS
  camera
  fusion
  perception
  planning
  control
  actuator
  camera_fusion
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
