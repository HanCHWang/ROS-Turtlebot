#!/usr/bin/env python
import rospy
import pickle
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
#from sklearn.ensemble import RandomForestClassifier
import numpy as np

class follower:
    def __init__(self):
        rospy.loginfo('Follower node initialized')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        #self.clf = pickle.load( open( "clf", "rb"))
        #self.clf2 = pickle.load( open( "clf2", "rb"))
        #self.labels = {'30_0':0, '30_l':1, '30_r':2, '45_0':3, '45_l':4, '45_r':5,'15_0':6, 'empty':7}
        rospy.loginfo('Tree initialized')
        self.follow() 
    def follow(self):
        laser_data=[]
        #laser_data_set=[]
        
        while not rospy.is_shutdown():
            self.msg = rospy.wait_for_message("/scan_filtered", LaserScan)
            
'''----------------------------------------------------------------------------------------------------------------------------------------------
            for i in range(70,-2,-1) + range(359, 289,-1):

                if   np.nan_to_num( self.msg.[i] ) != 0 :
                     laser_data.append(np.nan_to_num(self.msg.intensities[i]))

                elif (i+1) in range(70,-2,-1) + range(359, 289,-1) and (i-1) in range(70,-2,-1) + range(359, 289,-1) and np.nan_to_num(self.msg.intensities[i]) == 0:
                     laser_data.append((np.nan_to_num(self.msg.intensities[i+1])+np.nan_to_num(self.msg.intensities[i-1]))/2)

                else :
                     laser_data.append(np.nan_to_num(self.msg.intensities[i]))

            #laser_data_set.append(laser_data)
  -------------------------------------------------------------------------------------------------------------------------------------------'''
  #above is the auth's data usage.
  #these are mine
        for i in range(0,359,1)
            laser_data[i]=self.msg.ranges[i]##just append every angle's distance to laser_data[]
            


        
            twist = Twist()
            twist.linear.x=laser_data[20]
            
            print twist.linear.x
            self.pub.publish(twist)
       # def avoid_ob(self)##try to avoid obstacle

def main():

    rospy.init_node('follower', anonymous=True)

    try:
        follow = follower()
        
        
    except rospy.ROSInterruptException:
        pass    #print("Shutting down")

if __name__ == '__main__':
    main()
