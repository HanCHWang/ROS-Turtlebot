#!/usr/bin/env python
import rospy
import pickle
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
#from sklearn.ensemble import RandomForestClassifier
import numpy as np


def main():
    f1=open("/home/iwin1/catkin_ws/src/president/scripts/data/posx.txt","r")
    f2=open("/home/iwin1/catkin_ws/src/president/scripts/data/posy.txt","r")
    f3=open("/home/iwin1/catkin_ws/src/president/scripts/data/goalx.txt","r")
    f4=open("/home/iwin1/catkin_ws/src/president/scripts/data/goaly.txt","r")
    line=f1.readlines()
    while line:
        print line
        line = f1.readlines()
        pass

if __name__ == '__main__':
    main()
