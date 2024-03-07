cmake_minimum_required(VERSION 3.8)
project(simple-chain)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# add_executable(camera src/camera.cpp)
# add_executable(fusion src/fusion.cpp)
# add_executable(perception src/perception.cpp)
# add_executable(planning src/planning.cpp)
# add_executable(control src/control.cpp)
# add_executable(actuator src/actuator.cpp)

# ament_target_dependencies(camera rclcpp std_msgs)
# ament_target_dependencies(fusion rclcpp std_msgs)
# ament_target_dependencies(perception rclcpp std_msgs)
# ament_target_dependencies(planning rclcpp std_msgs)
# ament_target_dependencies(control rclcpp std_msgs)
# ament_target_dependencies(actuator rclcpp std_msgs)

add_executable(1-ste
               src/1-ste.cpp
               src/camera.cpp
               src/fusion.cpp
               src/perception.cpp
               src/planning.cpp
               src/control.cpp
               src/actuator.cpp
)
ament_target_dependencies(1-ste rclcpp std_msgs)

add_executable(1-mte
               src/1-mte.cpp
               src/camera.cpp
               src/fusion.cpp
               src/perception.cpp
               src/planning.cpp
               src/control.cpp
               src/actuator.cpp
)
ament_target_dependencies(1-mte rclcpp std_msgs)

add_executable(n-ste
               src/n-ste.cpp
               src/camera.cpp
               src/fusion.cpp
               src/perception.cpp
               src/planning.cpp
               src/control.cpp
               src/actuator.cpp
)
ament_target_dependencies(n-ste rclcpp std_msgs)

add_executable(n-mte-per-1-node
               src/n-mte-per-1-node.cpp
               src/camera.cpp
               src/fusion.cpp
               src/perception.cpp
               src/planning.cpp
               src/control.cpp
               src/actuator.cpp
)
ament_target_dependencies(n-mte-per-1-node rclcpp std_msgs)

add_executable(n-mte-per-2-node
               src/n-mte-per-2-node.cpp
               src/camera.cpp
               src/fusion.cpp
               src/perception.cpp
               src/planning.cpp
               src/control.cpp
               src/actuator.cpp
)
ament_target_dependencies(n-mte-per-2-node rclcpp std_msgs)

install(TARGETS
  1-ste
  1-mte
  n-ste
  n-mte-per-1-node
  n-mte-per-2-node
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
