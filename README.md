# SEA:ME@Korea 2024 Summer Hackathon<br>

During this hackathon, your mission is to develop a autonomous driving system based on JetRacer Pro. We'll provide you an Nvidia Jetson nano embedded board. 

https://www.waveshare.com/wiki/JetRacer_Pro_AI_Kit

## Step 0: Assemble your JetRacer Pro
[Jetracer_pro_Assembly_EN.pdf](https://github.com/user-attachments/files/16007743/Jetracer_pro_Assembly_EN.pdf)

## Step 1: Install Image
1. Download the JetRacer image and unzip it.

[https://drive.google.com/file/d/1ZBdqrwhW2n1uN8rughF7Puw98o76kUcH/view?usp=sharing]

2. Download Etcher.

https://github.com/balena-io/etcher/releases/download/v1.19.21/balenaEtcher-1.19.21.Setup.exe

3. Write the image using Etcher.

![image](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/27d577d6-3ba9-4511-930e-979d170aa077)

## Step 2: Initial setup
1. Insert SD card to SD card slot of Jetson Nano (the slot is on the back of Jetson Nano module)
```
Picture?
```

2. Power on JetRacer AI Kit
```
Picture?
```

#####ADD VNC remote control#####

3. Connect WIFI

4. Run the following commands on the terminal
```bash 
cd ~/jetracer
git checkout ws/pro
sudo python3 setup.py install
sudo reboot
```

5. Configure Power Mode
>You need to launch a new Terminal and enter the following commands to select 5W power mode.
```bash
sudo nvpmodel -m1
```

6. Resize disk partition
```
sudo apt update
sudo apt install gparted
sudo gparted
```
>Resize partition to maxsize

![3](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/1a451278-ae0e-4fa4-a956-d33571ff38c5)

## Step 3. Fix the apt upgrade error
```
sudo apt update
sudo apt upgrade
```

>If you see this error

![apt_upgrade_error](https://github.com/SeungWoo3/jetracer/assets/78201406/5131c1a9-b7fd-421c-9ce1-b98dba039c8f)

>Execute the lines below

```
sudo mv /var/lib/dpkg/info/ /var/lib/dpkg/info_old/
sudo mkdir /var/lib/dpkg/info
sudo apt update
sudo apt -f install
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old/
sudo rm -rf /var/lib/dpkg/info
sudo mv /var/lib/dpkg/info_old/ /var/lib/dpkg/info/
sudo apt update
sudo apt upgrade
```

## Step 4. Install ROS (melodic)
http://wiki.ros.org/melodic/Installation/Ubuntu  

1. Setup your sources.list
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2. Set up your keys
```
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

3. Installation
```
sudo apt update   
sudo apt install ros-melodic-desktop-full
```

4. Environment setup
```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/melodic/setup.bash
```

5. Dependencies for building packages
>python 2.7
```
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```
>python3(essential)
```
sudo apt install python3-pip python3-all-dev python3-rospkg
sudo apt install ros-melodic-desktop-full --fix-missing
```
If you make a python ros package, you should add this line at the top of python script
```python
#!~/usr/bin/env python3
```
6. Create a ROS Workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws
catkin_make
```
>python3 (optional)
```
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```

## Step 5. Install ROS Packages
### joy controller
1. Check controller connection in https://hardwaretester.com/gamepad
>#Waiting for connection
![1](https://github.com/SeungWoo3/jetracer/assets/117966644/006ea758-bcf1-46fd-8e5c-c890bb4ee344)
>#Connection successful
![2](https://github.com/SeungWoo3/jetracer/assets/117966644/742b7db2-373e-4b68-85b1-b6b0e43f947b)

2. Install the package & Run
```
sudo apt install ros-melodic-teleop-twist-joy
rosrun joy joy_node
```

3. Check the ros topic
```
rostopic echo /joy
```

### usb_cam
```
sudo apt install ros-melodic-usb-cam
```

## Step 6. OpenCV settings
```
sudo gedit /opt/ros/melodic/share/cv_bridge/cmake/cv_bridgeConfig.cmake
```
>In line 96
```
-- set(_include_dirs "include;/usr/include;/usr/include/opencv")
++ set(_include_dirs "include;/usr/include;/usr/include/opencv4") 
```

>In line 119
```
-- set(libraries "cv_bridge;/usr/lib/aarch64-linux-gnu/libopencv_core.so.3.2.0;/usr/lib/aarch64-linux-gnu/libopencv_imgproc.so.3.2.0;/usr/lib/aarch64-linux-gnu/libopencv_imgcodecs.so.3.2.0") 
++ set(libraries "cv_bridge;/usr/lib/aarch64-linux-gnu/libopencv_core.so.4.1.1;/usr/lib/aarch64-linux-gnu/libopencv_imgproc.so.4.1.1;/usr/lib/aarch64-linux-gnu/libopencv_imgcodecs.so.4.1.1") 
```

