#!/usr/bin/env python

import rospy
import sys
from sensor_msgs.msg import Joy
import time
# ROS Node converts Joystick inputs from the joy node

from robot_api import *

# set the *_max values below to control max values
# currenty left and right are scaled.
# vertical are the actual values used
motor1_max = 10.0
motor2_max = 10.0
motor3_max = 10.0
motor4_max = 10.0
motor5_max = 10.0
motor6_max = 10.0
current_time = 14.8
command_time = 0.9

motor1_cmd = 0
motor2_cmd = 0
motor3_cmd = 0
motor4_cmd = 0
motor5_cmd = 0 
motor6_cmd = 0

def joy_callback(data):
	print('Received joystick message') 
	#print data.axes 
	
	global motor1_cmd, motor2_cmd, motor3_cmd, motor4_cmd, motor5_cmd, motor6_cmd
	motor1_cmd = 0
	motor2_cmd = 0
	motor3_cmd = 0
	motor4_cmd = 0
	motor5_cmd = 0 
	motor6_cmd = 0
   
	# Set right and left thruster command  
	# Set to use just one joystick. So other joystick can control vertical
	if (data.axes[1] > 0.3): # filter out really small values
	        motor1_cmd = int(data.axes[1] * motor1_max * -1)
	if (data.axes[1] < -0.3):
	        motor1_cmd = int(abs(data.axes[1]) * motor1_max)
	
	if (data.axes[4] > 0.3): # filter out really small values
		motor2_cmd = int(data.axes[4] * motor2_max * -1)
	if (data.axes[4] < -0.3):
		motor2_cmd = int(abs(data.axes[4]) * motor2_max)

	if (data.axes[7] > 0.8):
		motor3_cmd = motor3_max
	if (data.axes[7] < -0.8):
		motor3_cmd = -1 *motor3_max
		
	if (data.axes[2] > 0.3): # filter out really small values
	        motor4_cmd = int(data.axes[2] * motor4_max * -1)
	if (data.axes[2] < -0.3):
	        motor4_cmd = int(abs(data.axes[2]) * motor4_max)
	
	if (data.axes[3] > 0.3): # filter out really small values
		motor5_cmd = int(data.axes[3] * motor5_max * -1)
	if (data.axes[3] < -0.3):
		motor5_cmd = int(abs(data.axes[3]) * motor5_max)

	if (data.axes[5] > 0.8):
		motor6_cmd = motor6_max
	if (data.axes[5] < -0.8):
		motor6_cmd = -1 *motor6_max
	

def listener(args):
	print "Starting Controller\n"	    
	# Connect to robot  
	v = xyzAPI()
	v.connect('xyz',100)

	# enable power for the onboard camera
	v.toggle_camera(True)
	v.send_command()	

        rospy.init_node('joy_listen')
	rospy.Subscriber("joy",Joy,joy_callback, queue_size=1)

        rate = rospy.Rate(5) # in Hz
	while not rospy.is_shutdown():
		v.set_velocity(motor1_cmd,motor2_cmd, motor3_cmd, motor4_cmd, motor5_cmd, motor6_cmd)
        	v.send_command()
		print "Sending Commands One:", motor1_cmd, " Two:", motor2_cmd, "Three:", motor3_cmd, "Four:", motor4_cmd, "Five:", motor5_cmd, "Six:", motor6_cmd ".\n"
		rate.sleep()
	
	rospy.spin()

if __name__ == '__main__':
	listener(sys.argv)