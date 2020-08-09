#!/usr/bin/env python

#Subscripbes to /Joy
# Publishes to /cmd_vel

#Using Left Trigger for throttle (forward)
#Using Right Stick for steering
#Usinf Right Trigger for (reverse)
#Using start button for boost setting (throttle multiplier)

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Map from xbox one remote to joy: https://wiki.ros.org/joy
# axes = [LS_lr, LS_ud, LT, RS_lr, RS_ud, RT, D_lr, D_ud]

def callback(data):
    twist = Twist()
    #twist.linear.x = ((-1)*data.axes[5] - (-1)*data.axes[2])*(0.35)
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[3]
    pub.publish(twist)

def start():
    rospy.loginfo("Setting Up the Node...")
    rospy.init_node('teleop_twist_xbox1_joy')
    rospy.loginfo("Node init complete")

    global pub
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

    rospy.Subscriber("joy", Joy, callback)

    rospy.spin()

if __name__ == '__main__':
    start()
    
