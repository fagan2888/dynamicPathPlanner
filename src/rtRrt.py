#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def move():
    pub1 = rospy.Publisher('/dynamicPathPlanner/world_base_1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/dynamicPathPlanner/world_base_2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('remote', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data1 = -10
        data2 = -10
        rospy.loginfo(data1)
        rospy.loginfo(data2)
        pub1.publish(data1)
        pub2.publish(data2)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass