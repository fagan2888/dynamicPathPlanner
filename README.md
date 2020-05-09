# DynamicPathPlanner
Repo for project 5 in path planning course.

## Author
- Pruthvi Sanghavi
- Achal Vyas

## Dependencies
- ROS
- Numpy
- Matplotlib
- pygame

## Install turtlebot stack
```
sudo apt-get install ros-kinetic-turtlebot-gazebo 
```

## Build Instructions
Open a terminal and type in the following,
```
mkdir <workspace>
cd <workspace>
mkdir src
cd src
git clone https://github.com/Pruthvi-Sanghavi/dynamicPathPlanner.git
cd ..
catkin_make
```
## Install Controllers
Open a terminal and type,
```
sudo apt-get install ros-kinetic-gazebo-ros-control
sudo apt-get install ros-kinetic-joint-state-controller
sudo apt-get install ros-kinetic-effort-controllers
sudo apt-get install ros-kinetic-position-controllers

```

## Steps
1. Make urdf. Import transmission and gazebo controller plugin.
2. Make launch file for spawning the robot and spawning the controller.
3. Make a config.yaml file.

## To run the code in python
Open a terminal,

```
cd <workspace>/src/dynamicPathPlanner/src
python rrtstar
```


## Run Instructions
Open a terminal, and type
```
cd <workspace>
source devel/setup.bash
roslaunch dynamicPathPlanner launcher.launch
```
- Click on the screen to enter the start point and the goal point and press escape to exit.
Open another terminal and type,
```
cd <workspace>
source devel/setup.bash
roslaunch dynamicPathPlanner controller.launch 
```

Open another terminal and type,
```
rostopic list
rostopic pub /<topic>
```



