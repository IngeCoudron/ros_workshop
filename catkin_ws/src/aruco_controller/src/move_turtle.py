#!/usr/bin/env python
 
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
from cv2 import aruco
import sys
 
def callback(msg):
    # Convert msg to frame:
    try:
        frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    
    # Detect marker
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    _, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if not ids is None:
        rospy.loginfo("Marker id: %d" % ids[0])
        
        # Convert to velocity command
        switcher = {
            6: (1.0, 0.0),  # UP
            2: (0.0, -1.0), # RIGHT
            4: (-1.0, 0.0), # DOWN
            5: (0.0, 1.0)   # LEFT
        }
        linear_, angular_ = switcher[int(ids[0])]
        
        # Publish velocity command
        cmd = Twist()
        cmd.linear.x = linear_
        cmd.angular.z = angular_ 
        pub.publish(cmd)
        
    
rospy.init_node('move_turtle', anonymous=True)
bridge = CvBridge()
pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=1)
sub = rospy.Subscriber('camera/image',Image,callback)
 
rospy.spin()
