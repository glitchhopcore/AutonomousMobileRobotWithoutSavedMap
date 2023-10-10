#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolRequest

rospy.init_node("client_node")
client = rospy.ServiceProxy("test_service", SetBool)
client.wait_for_service()

request = SetBoolRequest()
request.data = True
response = client(request)
print(response)
