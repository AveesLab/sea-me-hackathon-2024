#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
# from jetracer.nvidia_racecar import NvidiaRacecar
from std_msgs.msg import Float32

# car = NvidiaRacecar()
MAX_SPEED = 0.2
pub_steering = rospy.Publisher('/Steering', Float32, queue_size=1)
pub_throttle = rospy.Publisher('/Throttle', Float32, queue_size=1)

def callback_joy(joy_msg):
	rospy.loginfo("steering: %f", -joy_msg.axes[2])
	rospy.loginfo("throttle: %f", joy_msg.axes[1])
	pub_steering.publish(-joy_msg.axes[2])
	if joy_msg.axes[1] < 0:
		weight = MAX_SPEED * 1.3
	else:
		weight = MAX_SPEED
	pub_throttle.publish(joy_msg.axes[1] * weight)
	# car.steering = -joy_msg.axes[2]
	# car.throttle = joy_msg.axes[1] * MAX_SPEED

def main():
	rospy.init_node('teleop', anonymous=False)
	rospy.loginfo('teleop node initiated!')
	rospy.Subscriber("/joy", Joy, callback_joy)
	rospy.spin()

if __name__ == "__main__":
	main()
