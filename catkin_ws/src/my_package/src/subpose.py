#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose


def pose_msg_received(msg):
  rospy.loginfo("Pose: (%.2f,%.2f,%.2f)" %(msg.x, msg.y, msg.theta))


rospy.init_node('subscribe_to_pose', anonymous=True)

sub = rospy.Subscriber('/turtle1/pose', Pose, pose_msg_received)

rospy.spin()

