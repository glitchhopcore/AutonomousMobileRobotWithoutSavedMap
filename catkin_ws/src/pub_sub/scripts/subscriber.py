#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

#callback func
def callback(msg):
    print(msg)

#node+topic init
rospy.init_node("subscriber_node")
rospy.Subscriber("topic", Int64, callback)

#spinning
rospy.spin()
