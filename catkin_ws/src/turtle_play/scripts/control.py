#!/usr/bin/env python3

import rospy 
import random 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(msg):
    print(msg)

rospy.init_node("control_node")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 1)
rospy.Subscriber("/turtle1/pose", Pose, callback)
msg = Twist()
#msg.angular.z = random.randint(0, 3)
#msg.linear.x = random.randint(0, 2)

for i in range(5):
    msg.angular.z = random.randint(0, 3) - 6
    msg.linear.x = random.randint(0, 2) - 4
    pub.publish(msg)
    rospy.sleep(1)

#rospy.spin()
