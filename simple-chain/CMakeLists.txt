cmake_minimum_required(VERSION 3.8)
project(simple-chain)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(yaml-cpp REQUIRED)

include_directories(include)

add_executable(1-ste
               src/1-ste.cpp
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
)
ament_target_dependencies(1-ste rclcpp std_msgs)

add_executable(1-mte
               src/1-mte.cpp
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
)
ament_target_dependencies(1-mte rclcpp std_msgs)

add_executable(n-ste
               src/n-ste.cpp
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(n-ste rclcpp std_msgs)
target_link_libraries(n-ste yaml-cpp)


add_executable(n-mte-per-1-node
               src/n-mte-per-1-node.cpp
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(n-mte-per-1-node rclcpp std_msgs)
target_link_libraries(n-mte-per-1-node yaml-cpp)

add_executable(n-mte-per-2-node
               src/n-mte-per-2-node.cpp
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(n-mte-per-2-node rclcpp std_msgs)
target_link_libraries(n-mte-per-2-node yaml-cpp)

add_executable(two_nodes_s1
               src/tasks/camera.cpp
               src/tasks/fusion.cpp
               src/tasks/perception.cpp
               src/tasks/planning.cpp
               src/tasks/control.cpp
               src/tasks/actuator.cpp
               src/two_nodes_s1.cpp
               src/tasks/talker.cpp
               src/tasks/listener.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(two_nodes_s1 rclcpp std_msgs)
target_link_libraries(two_nodes_s1 yaml-cpp)

add_executable(two_nodes_s2
               src/two_nodes_s2.cpp
               src/tasks/talker.cpp
               src/tasks/listener.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(two_nodes_s2 rclcpp std_msgs)
target_link_libraries(two_nodes_s2 yaml-cpp)

add_executable(two_nodes_m1
               src/two_nodes_m1.cpp
               src/tasks/talker.cpp
               src/tasks/listener.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(two_nodes_m1 rclcpp std_msgs)
target_link_libraries(two_nodes_m1 yaml-cpp)

add_executable(two_nodes_m2
               src/two_nodes_m2.cpp
               src/tasks/talker.cpp
               src/tasks/listener.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(two_nodes_m2 rclcpp std_msgs)
target_link_libraries(two_nodes_m2 yaml-cpp)

install(TARGETS
  1-ste
  1-mte
  n-ste
  n-mte-per-1-node
  n-mte-per-2-node
  two_nodes_s1
  two_nodes_s2
  two_nodes_m1
  two_nodes_m2
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY 
  config
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
