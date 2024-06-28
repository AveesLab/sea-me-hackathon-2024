#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def main():
    pub_steering = rospy.Publisher('/Steering', Float32, queue_size=1)
    pub_throttle = rospy.Publisher('/Throttle', Float32, queue_size=1)
    rospy.init_node('manual_control', anonymous=False)
    rospy.loginfo('manual_control node initiated!')

    rate = rospy.Rate(1) # 10hz
    i = 0
    while not rospy.is_shutdown():
        if i==0:
            i = 1
            steering = 0.5
            throttle = 0
        else:
            i = 0
            steering = -0.5
            throttle = 0.2
        pub_steering.publish(steering)
        pub_throttle.publish(throttle)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass