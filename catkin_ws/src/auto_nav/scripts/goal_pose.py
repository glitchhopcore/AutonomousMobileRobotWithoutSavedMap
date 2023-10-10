#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def active_cb(extra):
    rospy.loginfo("Goal Pose Is Being Processed...")

def feedback_cb(feedback):
    rospy.loginfo("Current Location: " + str(feedback))
    
def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal Reached.")
    if status == 3 or status == 8:
        rospy.loginfo("Goal Cancelled.")
    if status == 4:
        rospy.loginfo("Goal Aborted.")

rospy.init_node('goal_pose_node')

navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
navclient.wait_for_server()

#Example Goal Location

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

goal.target_pose.pose.position.x = 2.0
goal.target_pose.pose.position.y = 0.5
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.65
goal.target_pose.pose.orientation.w = 0.75

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()

if not finished:
    rospy.logerr("Action Server Not Available")
else:
    rospy.loginfo(navclient.get_result())
