#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

steering = 0
throttle = 0
is_moving = False
pub_steering = rospy.Publisher('/Steering', Float32, queue_size=1)
pub_throttle = rospy.Publisher('/Throttle', Float32, queue_size=1)

def callback_dist(dist_msg):
	rospy.loginfo("dist: %f", dist_msg.data)
	dist = dist_msg.data

	global is_moving
	global steering
	global throttle

	if 0<dist<15 and is_moving == True:
		rospy.loginfo("brake activated!")
		throttle = 0
		is_moving = False
	elif dist>15 or dist<0:
		rospy.loginfo("running!")
		throttle = 0.2
		is_moving = True
	pub_steering.publish(steering)
	pub_throttle.publish(throttle)

def main():
	rospy.init_node('demo', anonymous=False)
	rospy.loginfo('demo node initiated!')

	rospy.Subscriber("/distance", Float32, callback_dist)
	
	global is_moving
	global steering
	global throttle

	throttle = 0.2
	is_moving = True
	rospy.spin()
		
	   


if __name__ == "__main__":
	main()
