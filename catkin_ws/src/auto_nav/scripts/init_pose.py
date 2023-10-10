#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

#Node Initialization 
rospy.init_node('init_pose_node')
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)

#Construct Message 
init_msg = PoseWithCovarianceStamped()
init_msg.header.frame_id = "map"

#Get Initial Pose From Gazebo
odom_msg = rospy.wait_for_message('/odom', Odometry)
init_msg.pose.pose.position.x = odom_msg.pose.pose.position.x
init_msg.pose.pose.position.y = odom_msg.pose.pose.position.y
init_msg.pose.pose.position.z = odom_msg.pose.pose.position.z

init_msg.pose.pose.orientation.x = odom_msg.pose.pose.orientation.x
init_msg.pose.pose.orientation.y = odom_msg.pose.pose.orientation.y
init_msg.pose.pose.orientation.z = odom_msg.pose.pose.orientation.z
init_msg.pose.pose.orientation.w = odom_msg.pose.pose.orientation.w

#Delay 
rospy.sleep(1)

#Publish Message
rospy.loginfo("Setting Initial Position...")
pub.publish(init_msg)
rospy.loginfo("Initial Pose Is Set.")
