#!/usr/bin/env python

import rospy
import geometry_msgs.msg
import random

rospy.init_node('publish_velocity', anonymous=True)

pub = rospy.Publisher('turtle1/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

random.seed(9001)

rate = rospy.Rate(2)
while not rospy.is_shutdown():
    linear = random.uniform(0, 5)
    angular = random.vonmisesvariate(0,0)
    
    cmd = geometry_msgs.msg.Twist()
    cmd.linear.x = linear
    cmd.angular.z = angular

    pub.publish(cmd)
    rate.sleep()

