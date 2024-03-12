cmake_minimum_required(VERSION 3.8)
project(simple-chain)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

add_executable(1-ste
               src/1-ste.cpp
               src/task/camera.cpp
               src/task/fusion.cpp
               src/task/perception.cpp
               src/task/planning.cpp
               src/task/control.cpp
               src/task/actuator.cpp
)
ament_target_dependencies(1-ste rclcpp std_msgs)

add_executable(1-mte
               src/1-mte.cpp
               src/task/camera.cpp
               src/task/fusion.cpp
               src/task/perception.cpp
               src/task/planning.cpp
               src/task/control.cpp
               src/task/actuator.cpp
)
ament_target_dependencies(1-mte rclcpp std_msgs)

add_executable(n-ste
               src/task/n-ste.cpp
               src/task/camera.cpp
               src/task/fusion.cpp
               src/task/perception.cpp
               src/task/planning.cpp
               src/task/control.cpp
               src/task/actuator.cpp
)
ament_target_dependencies(n-ste rclcpp std_msgs)

add_executable(n-mte-per-1-node
               src/n-mte-per-1-node.cpp
               src/task/camera.cpp
               src/task/fusion.cpp
               src/task/perception.cpp
               src/task/planning.cpp
               src/task/control.cpp
               src/task/actuator.cpp
)
ament_target_dependencies(n-mte-per-1-node rclcpp std_msgs)

add_executable(n-mte-per-2-node
               src/n-mte-per-2-node.cpp
               src/task/camera.cpp
               src/task/fusion.cpp
               src/task/perception.cpp
               src/task/planning.cpp
               src/task/control.cpp
               src/task/actuator.cpp
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
