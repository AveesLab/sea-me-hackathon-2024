cmake_minimum_required(VERSION 3.0.2)
project(todo)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

find_package(OpenCV REQUIRED)
catkin_package()

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

set(PROJECT_SOURCES
  src/todo.cpp
)

add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})

target_link_libraries(${PROJECT_NAME}
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
)
