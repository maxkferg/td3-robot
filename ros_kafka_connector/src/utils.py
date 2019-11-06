#!/usr/bin/env python

def import_msg_type(msg_type):

    # Adding a new msg type is as easy as including an import and updating the variable 
    if msg_type == "std_msgs/String":
        from std_msgs.msg import String
        subscriber_msg = String
    elif msg_type == "geometry_msgs/Twist":
        from geometry_msgs.msg import Twist
        subscriber_msg = Twist
    elif msg_type == "sensors_msgs/Image":
        from sensor_msgs.msg import Image
        subscriber_msg = Image
    elif msg_type == "sensor_msgs/PointCloud2":
        from sensor_msgs.msg import PointCloud2
        subscriber_msg = PointCloud2
    elif msg_type == "kobuki_msgs/BumperEvent":
        from kobuki_msgs.msg import BumperEvent
        subscriber_msg = BumperEvent
    elif msg_type == "sensor_msgs/Imu":
        from sensor_msgs.msg import Imu
        subscriber_msg = Imu
    elif msg_type == "nav_msgs/Odometry":
        from nav_msgs.msg import Odometry
        subscriber_msg = Odometry
    elif msg_type == "nav_msgs/OccupancyGrid":
        from nav_msgs.msg import OccupancyGrid
        subscriber_msg = OccupancyGrid
    else:
        raise ValueError("MSG NOT SUPPORTED: %s. \
                          Please add imports to utils.py for specific msg type.",msg_type)
    
    return subscriber_msg
