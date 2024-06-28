#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from jetracer.nvidia_racecar import NvidiaRacecar

car = NvidiaRacecar()

def callback_steering(steering):
    rospy.loginfo("steering: %f", steering.data)
    car.steering = steering.data

def callback_throttle(throttle):
    rospy.loginfo("throttle: %f", throttle.data)
    car.throttle = throttle.data

def main():
    rospy.init_node('actuator', anonymous=False)
    rospy.loginfo('jetracer node initiated!')
    rospy.Subscriber("/Steering", Float32, callback_steering)
    rospy.Subscriber("/Throttle", Float32, callback_throttle)
    rospy.spin()

if __name__ == '__main__':
    main()
