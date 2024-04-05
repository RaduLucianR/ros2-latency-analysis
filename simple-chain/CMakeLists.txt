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

add_executable(exec_archi
               src/exec_archi.cpp
               src/tasks/templnode.cpp
               src/utils/cpu_affinity_utils.cpp
)
ament_target_dependencies(exec_archi rclcpp std_msgs)
target_link_libraries(exec_archi yaml-cpp)

install(TARGETS
  exec_archi
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
