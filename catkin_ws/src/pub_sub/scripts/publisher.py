#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

#node+topic init
rospy.init_node("publisher_node")
pub = rospy.Publisher("topic", Int64, queue_size = 1)

#looping
while not rospy.is_shutdown():
    pub.publish(1)
    rospy.sleep(1)
