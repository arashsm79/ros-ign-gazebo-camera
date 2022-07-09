# ros 2 <-> ign gazebo camera sensor example
> A simple example demonstrating the use of ros_ign_bridge to enable the exchange of messages between ignition gazebo and ros 2. A camera sensor is included in a world containing a box.

Components:
* [setup.py](#setup)
* [Launch File](#launch-file)
* [World and Models](#world-and-models)
* [Screenshots](#screenshots)



# setup
In `setup.py` we have to make sure that our world and models are copied properly to the install location. We do this by specifying them in the `data_files` array.
```python
    data_files=[
        ...,
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "worlds"), glob('worlds/*.sdf')),
        (os.path.join('share', package_name, "models", "arashcamera"), glob('models/arashcamera/*')),
    ],
```

# Launch File
First using the `IGN_GAZEBO_RESOURCE_PATH` environment variable we have to specify the path to our models' directory in the install location so that ign gazebo would be able to find our sensor.

Then we create 3 components:
  - A process to launch gazebo
  - A ros node to spin up rviz 2
  - The ros_ign_bridge to connect ign topics to that of ros 2
  
# World and Models
In the `worlds` directory, there is a simple sdf file that contains a box, a plane, and a sun. We have also included our camera sensor in this file using the `<include>` tag.

In the `models` directory lives our camera sensor which is a simple sdf file containing the sensor and its description.

# Screenshots
![gazebo](/screenshots/gazebo.png)

![rviz2](/screenshots/rviz.png)
