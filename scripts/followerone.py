#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg="""
president does magic to himself
"""

global twist
twist=Twist()

global call_back_data
call_back_data=Twist()

def Rotate():
    twist.linear.x=0.5
    twist.angular.z=2.0
    print msg
    
    #rospy.loginfo()
def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
def callback(data):
    call_back_data.linear.x=data.linear.x
    call_back_data.angular.z=data.angular.z
    rospy.loginfo("""the linear_vel is""")
    print call_back_data.linear.x
    rospy.loginfo("""the angular_vel is""")
    print call_back_data.angular.z
    pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
    pub.publish(call_back_data)
    
if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('followerone',)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('leader_twist',Twist,callback)
    try:
        print msg
        while not rospy.is_shutdown():
            
            key = getKey()
            twist = Twist()

            '''
            twist.linear.x = 1.0; twist.linear.y = 0.0; twist.linear.z = 0.0

            
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 1.0
            '''
            #print 2
            if (key == '\x03'):
                break
            
            rospy.Subscriber('/leader_twist',Twist,callback)
            #pub.publish(call_back_data)
            rospy.spin()
            #pub.publish(call_back_data)

            #pub.publish(call_back_data)
            #print call_back_data.linear.x
            
    except:
        print """presidentnb"""

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        print twist.linear.x
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    
