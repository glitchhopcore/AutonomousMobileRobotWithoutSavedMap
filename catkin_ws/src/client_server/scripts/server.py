#!/usr/bin/env python3
import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def callback(req):
    response = SetBoolResponse()
    if req.data == True:
        response.success = True
        response.message = "Enabled"
    else:
        respone.success = True
        response.message = "Disabled"
    return response

rospy.init_node("server_node")
rospy.Service("test_service", SetBool, callback)
rospy.spin()
