#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def main():
    pub_steering = rospy.Publisher('/Steering', Float32, queue_size=10)
    pub_throttle = rospy.Publisher('/Throttle', Float32, queue_size=10)
    rospy.init_node('e-stop', anonymous=False)
    rospy.loginfo('e-stop node initiated!')
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo('e-stop')
        steering = 0
        throttle = 0
        pub_steering.publish(steering)
        pub_throttle.publish(throttle)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass