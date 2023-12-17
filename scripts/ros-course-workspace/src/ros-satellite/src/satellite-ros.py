#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import String

def satellite():
    pub = rospy.Publisher('commmand', String, queue_size=0)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1Hz
    cmd_list = ['w', 'a', 's', 'd']

    while not rospy.is_shutdown():
        str_cmd = cmd_list[random.radint(0, len(cmd_list))]
        rospy.loginfo(str_cmd)
        pub.publish(str_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        satellite()
    except rospy.ROSInterruptException:
        pass