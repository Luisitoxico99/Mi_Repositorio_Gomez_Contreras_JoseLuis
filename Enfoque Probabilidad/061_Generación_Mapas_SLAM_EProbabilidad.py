#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion
from gmapping import slam_gmapping
from threading import Thread

class SLAM:
    def __init__(self):
        rospy.init_node('slam_node')
        self.map_publisher = rospy.Publisher('/map', OccupancyGrid, queue_size=1)
        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.slam_thread = Thread(target=self.run_slam)
        self.slam_thread.start()

    def odom_callback(self, msg):
        quaternion = (
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w)
        _, _, yaw = euler_from_quaternion(quaternion)
        # Actualizar la posición del robot

    def scan_callback(self, msg):
        # Pasar los datos del escáner láser al algoritmo SLAM

    def run_slam(self):
        slam_gmapping()

if __name__ == '__main__':
    SLAM()
    rospy.spin()
