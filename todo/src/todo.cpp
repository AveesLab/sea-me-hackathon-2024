#include <iostream>
#include "ros/ros.h"

#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/Joy.h>
#include <std_msgs/Header.h>
#include <std_msgs/Float32.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

float dist;
cv::Mat camImageCopy_;

void ImageSubCallback(const sensor_msgs::ImageConstPtr& msg){
    cv_bridge::CvImagePtr cam_image;
    try{
        cam_image = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    } catch (cv_bridge::Exception& e) {
        ROS_ERROR("cv_bridge exception : %s", e.what());
    }

    if(!cam_image->image.empty()) {
        camImageCopy_ = cam_image->image.clone();
    }
}

void DistanceSubCallback(const std_msgs::Float32& dist_msg){
    dist = dist_msg.data;
}

void JoySubCallback(const sensor_msgs::Joy& joy_msg){
    
}


int main(int argc, char **argv){
    ros::init(argc, argv, "todo");
    ros::NodeHandle nh;

    ros::Subscriber ImageSubscriber_ = nh.subscribe("/usb_cam/image_raw", 1, &ImageSubCallback);
    ros::Subscriber DistanceSubscriber_ = nh.subscribe("/distance", 1, &DistanceSubCallback);
    ros::Subscriber JoyeSubscriber_ = nh.subscribe("/joy", 1, &JoySubCallback);

    ros::Publisher steeringPublisher_ = nh.advertise<std_msgs::Float32>("/Steering", 1);
    ros::Publisher throttlePublisher_ = nh.advertise<std_msgs::Float32>("/Throttle", 1);
    std_msgs::Float32 steering_msg;
    std_msgs::Float32 throttle_msg;


    while(ros::ok()){
        ros::spinOnce();
        cv::namedWindow("image");
        if(!camImageCopy_.empty()){
            imshow("image", camImageCopy_);
        }
        ROS_INFO("dist: %f", dist);
        steering_msg.data = 0;
        throttle_msg.data = 0;
        steeringPublisher_.publish(steering_msg);
        throttlePublisher_.publish(throttle_msg);
    }
	return 0;
}
