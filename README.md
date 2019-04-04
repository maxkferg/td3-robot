# Mobile Robot Control Software

## Quick Start
### Build the current source
```sh
cd ~/td3_ws
export ROS_IP=10....
catkin_make_isolated --install --use-ninja
source install_isolated/setup.bash
```

### Record data to generate a map 
```
export MAP=/ssd/maps/lab.bag
roslaunch cartographer_turtlebot record.launch
roslaunch turtlebot_teleop keyboard_teleop.launch # In another terminal
mv /ssd/maps/scan_2019-04-03-18-22-49.bag $MAP
```

### Compute and save the map
```
roslaunch cartographer_turtlebot replay_offline.launch bag_filenames:=$MAP no_rviz:=True

roslaunch cartographer_turtlebot assets_writer.launch bag_filenames:=$MAP pose_graph_filename:=$MAP.pbstream
```

### Localize the robot in the map
This localizes the robot in $MAP and publishes the position using ROS_BRIDGE.
Other services can subscribe to the position by connnecting to the websocket on port 8080.
```
roslaunch cartographer_turtlebot localization.launch load_state_filename:=$MAP.pbstream no_rviz:=True
```

## Jetson Performance
The following commands can be used to improve Jetson performance:
```sh
sudo /sbin/iw dev wlan0 set power_save off
sudo ~/jetson_clocks.sh
```
