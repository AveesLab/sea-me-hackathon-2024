#include "ros/ros.h"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <cv_bridge/cv_bridge.h>


int main(int argc, char **argv){
    ros::init(argc, argv, "opencv_test");
    cv::Mat image = cv::imread("/home/jetson/catkin_ws/src/source.png", cv::IMREAD_COLOR);
    if (image.empty()){
        std::cerr << "Image Loaded Fail!" << std::endl;
        return -1;
    }
    std::cout<<"Image Loaded!"<<std::endl;
    cv::namedWindow("source");
    cv::imshow("source", image);
    cv::waitKey(-1);
        
    return 0;
}
