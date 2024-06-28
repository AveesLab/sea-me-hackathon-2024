<<<<<<< HEAD
# SEA:ME@Korea 2024 Summer Hackathon<br>

During this hackathon, your mission is to develop a atonomous driving system based on JetRacer Pro. We'll provide you an Nvidia Jetson nano embedded board. 

https://www.waveshare.com/wiki/JetRacer_Pro_AI_Kit


## Step 0: Assemble your JetRacer Pro

[https://files.waveshare.com/upload/f/fa/Jetracer_pro_Assembly_EN.pdf](https://files.waveshare.com/upload/f/fa/Jetracer_pro_Assembly_EN.pdf)



## Step 1: Install Image
1. Download the JetRacer image and unzip it.
   
 [https://drive.google.com/file/d/1ZBdqrwhW2n1uN8rughF7Puw98o76kUcH/view?usp=sharing](https://drive.google.com/file/d/1ZBdqrwhW2n1uN8rughF7Puw98o76kUcH/view?usp=sharing)
=======
# 2024 SEA:ME Hackathon<br>

During this hackathon, your mission is to develop a autonomous driving system based on JetRacer Pro. We'll provide you an Nvidia Jetson nano embedded board. 

![image](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/038d2832-94b0-416d-af1e-464430ddb012)


https://www.waveshare.com/wiki/JetRacer_Pro_AI_Kit

## Step 0: Assemble your JetRacer Pro
[Jetracer_pro_Assembly_EN.pdf](https://github.com/user-attachments/files/16007743/Jetracer_pro_Assembly_EN.pdf)

## Step 1: Install Image
1. Download the JetRacer image and unzip it.

[https://drive.google.com/file/d/1ZBdqrwhW2n1uN8rughF7Puw98o76kUcH/view?usp=sharing]
>>>>>>> 1a13bb8345cf2c917ba39a2854cb7734fb38a365

2. Download Etcher.

https://github.com/balena-io/etcher/releases/download/v1.19.21/balenaEtcher-1.19.21.Setup.exe

3. Write the image using Etcher.

<<<<<<< HEAD


## Step 2: Initial setup
1. Insert SD card to SD card slot of Jetson Nano (the slot is on the back of Jetson Nano module)
```
Picture?
```
2. Power on JetRacer AI Kit
```
Picture?
```
=======
![image](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/27d577d6-3ba9-4511-930e-979d170aa077)

## Step 2: Initial setup
1. Insert SD card to SD card slot of Jetson Nano (the slot is on the back of Jetson Nano module)

2. Power on JetRacer carrier board
>>>>>>> 1a13bb8345cf2c917ba39a2854cb7734fb38a365

3. Connect WIFI

4. Run the following commands on the terminal
```bash 
cd ~/jetracer
git checkout ws/pro
sudo python3 setup.py install
sudo reboot
```

5. Configure Power Mode
<<<<<<< HEAD
```bash
sudo nvpmodel -m1
```
<!--
## Step 3: Install OpenCV
1. Uninstall old version of OpenCV
```bash
sudo apt-get purge  libopencv* python-opencv
sudo apt-get autoremove
sudo find /usr/local/ -name "*opencv*" -exec rm -i {} \;
```


2. Install required libraries
```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get -y install build-essential cmake
sudo apt-get -y install pkg-config
sudo apt-get -y install libjpeg-dev libtiff5-dev libpng-dev
sudo apt-get -y install ffmpeg libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
sudo apt-get -y install libv4l-dev v4l-utils
sudo apt-get -y install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
sudo apt-get -y install libatlas-base-dev gfortran libeigen3-dev
sudo apt-get -y install python3-dev python3-numpy
```

3. Download OpenCV 4.4.0 source file
```bash
mkdir OpenCV && cd OpenCV
git clone -b 4.4.0 https://github.com/opencv/opencv
git clone -b 4.4.0 https://github.com/opencv/opencv_contrib
cd opencv && mkdir build && cd build
```

4. Build OpenCV 4.4.0
```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
-D WITH_OPENCL=OFF \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=7.2 \
-D CUDA_ARCH_PTX="" \
-D WITH_CUDNN=ON \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D WITH_QT=OFF \
-D WITH_OPENMP=ON \
-D WITH_OPENGL=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python3=TRUE \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF \
..
```
```bash
sudo make install -j8
```
5. 0.2.2 Environment setup
>~~~
>sudo vim /usr/lib/pkgconfig/opencv.pc
>~~~
>-add the below
>~~~
># Package Information for pkg-config
>prefix=/usr/local
>exec_prefix=${prefix}libdir=${exec_prefix}/lib/aarch64-linux-gnu
>includedir_old=${prefix}/include/opencv4/opencv
>includedir_new=${prefix}/include/opencv4
>
>Name: OpenCV
>Description: Open Source Computer Vision Library
>Version: 4.4.0
>Libs: -L${exec_prefix}/lib/aarch64-linux-gnu -lopencv_dnn -lopencv_gapi -lopencv_highgui -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_video -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_videoio -lopencv_imgcodecs -lopencv_imgproc -lopencv_core
>Libs.private: -ldl -lm -lpthread -lrt
>Cflags: -I${includedir_old} -I${includedir_new}
>~~~

6. 0.2.3 Jetson Stats
>~~~
>sudo -H pip3 install jetson-stats
>jeson_release
>~~~

7. 0.3.2 Environment setup
>-Setup the path
>~~~
>sudo cp -R /usr/local/lib/* /usr/lib
>~~~

-->
## Step 3. apt update
```bash
=======
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
>>>>>>> 1a13bb8345cf2c917ba39a2854cb7734fb38a365
sudo apt update
sudo apt upgrade
```

<<<<<<< HEAD
if you see this error

![apt_upgrade_error](https://github.com/SeungWoo3/jetracer/assets/78201406/5131c1a9-b7fd-421c-9ce1-b98dba039c8f)

execute the lines below

```bash
sudo mv /var/lib/dpkg/info/ /var/lib/dpkg/info_old/
sudo mkdir /var/lib/dpkg/info
sudo apt-get update
sudo apt-get -f install
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old/
sudo rm -rf /var/lib/dpkg/info
sudo mv /var/lib/dpkg/info_old/ /var/lib/dpkg/info/
sudo apt-get update
sudo apt-get upgrade
=======
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
>>>>>>> 1a13bb8345cf2c917ba39a2854cb7734fb38a365
```

## Step 4. Install ROS (melodic)
http://wiki.ros.org/melodic/Installation/Ubuntu  
<<<<<<< HEAD
cd ~/catkin_ws/src
1. Setup your sources.list
>```
>sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
>```
2. Set up your keys
>```
>sudo apt install curl
>curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
>```
3. Installation
>```
>sudo apt update   
>sudo apt install ros-melodic-desktop-full
>```
4. Environment setup
>```
>echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
>source ~/.bashrc
>source /opt/ros/melodic/setup.bash
>```
5. Dependencies for building packages
>### python 2.7
>```
>sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
>sudo apt install python-rosdep
>sudo rosdep init
>rosdep update
>```
>### python3(essential)
>```
>sudo apt install python3-pip python3-all-dev python3-rospkg
>sudo apt install ros-melodic-desktop-full --fix-missing
>```
>You should put following line at the top of python script
>```python
>#!~/usr/bin/env python3
>```
>
>## 1.6 Create a ROS Workspace
>```
>mkdir -p ~/catkin_ws/src
>cd ~/catkin_ws/src
>catkin_init_workspace
>cd ~/catkin_ws
>catkin_make
>```
>### python3 option
>```
>catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
>```
## Step 5. Install ROS Packages
### usb_cam
>```
>sudo apt install ros-melodic-usb-cam
>```

<!-- 
# 3. Install module & Environment setup
- melodic is ros-version (18.04 LTS)
>## 3.1 cv_bridge Setup
>- 3.1.1
>```
>vim ~/catkin_ws/src/vision_opencv/cv_bridge/CMakelist.txt
>```
>-fix the below
>```
>--find_package(Boost REQUIRED python37)
>++find_package(Boost REQUIRED python)
>```
>- 3.1.2
>```
>vim ~/catkin_ws/src/vision_opencv/cv_bridge/src/module.hpp
>```
>-fix the below
>```
>--static void * do_numpy_import( )
>++static void do_numpy_import( )
>--return nullptr;
>```

>## 3.2 rosserial_Arduino Module
>- communicate with OpenCR 1.0
>```
>sudo apt-get install ros-melodic-rosserial-arduino   
>sudo apt-get install ros-melodic-rosserial   
>```
>## 3.4 alias command Setup
>```
>sudo vim ~/.bashrc
>```
>-add the below
>```
>++source ~/catkin_ws/devel/setup.bash
>++alias cw='cd ~/catkin_ws'
>++alias cs='cd ~/catkin_ws/src'
>++alias cm='cd ~/catkin_ws && catkin_make'
>++alias cb='source ~/catkin_ws/devel/setup.bash'
>++alias sb='source ~/.bashrc'
>```
>```
>source ~/.bashrc
>```
>
>## 3.5 ros package build
>```
>cm
>```

-->


## Step 3. OpenCV settings
edit /opt/ros/melodic/share/cv_bridge/cmake/cv_bridgeConfig.cmake
In Ln96
change from
```
/usr/include/opencv
```
to
```
/usr/include/opencv4
```


In Ln119
change from (x3)
```
*.so.3.2.0
```
to
```
*.so.4.1.1
```

### check
```bash
git clone -b main https://github.com/SeungWoo3/jetracer.git
roslaunch usb_cam usb_cam-test.launch
rosrun lane_detect_image lane_detect_image_node
rosrun control control.py
rosrun control actuator.py
rqt_graph
```
You can see rqt_graph below
![rqt (1)](https://github.com/SeungWoo3/jetracer/assets/78201406/65fb5368-630e-4887-8a2c-032221f1ac13)


## Step 6. Arduino ultrasonic sensor setting
1. install ros package
```bash
sudo apt install ros-melodic-rosserial rosmelodic-rosserial-arduino
```
2. download Arduino
   
https://downloads.arduino.cc/arduino-1.8.19-linuxaarch64.tar.xz?_gl=1*cef7fs*_ga*ODQ1NTYxNzQ4LjE3MTgyNjE2NDc.*_ga_NEXN8H46L5*MTcxODI2MTY0Ni4xLjEuMTcxODI2MjkzMS4wLjAuMTcwNDA3OTI1MA

```bash
unzip arduino-1.8.19-linuxaarch64
sudo sh install.sh
```

After connect arduino and Jetson nano, check connection
```bash
ls -l /dev/ttyACM0
```


authorize
```bash
sudo usermod -a -G dialout jetson
sudo chmod a+rw /dev/ttyACM0
```

### check
```bash
roscore
rosrun rosserial_python serial_node.py -port:=/dev/ttyACM0 _baud:=9600
```
upload the ino file. Ino file is given by this github.















# jetracer
![6_21_result](https://github.com/SeungWoo3/jetracer/assets/78201406/c20118f2-6520-47d1-be59-eb5b0ac8a319)
=======

1. Setup your sources.list
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2. Setup your keys
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
### Joy controller
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

### Usb camera
```
sudo apt install ros-melodic-usb-cam
```

## Step 6. Edit openCV settings
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

>Check the settings
```
cd ~/catkin_ws/src
git clone https://github.com/AveesLab/sea-me-hackathon-2024.git
cd ../
catkin_make
```
```
roscore
rosrun opencv_test opencv_test
```



## Step 7. Use arduino ROS
1. install ros package
```
sudo apt install ros-melodic-rosserial ros-melodic-rosserial-arduino
```
2. download Arduino
   
>Install this file
- https://downloads.arduino.cc/arduino-1.8.19-linuxaarch64.tar.xz?_gl=1*cef7fs*_ga*ODQ1NTYxNzQ4LjE3MTgyNjE2NDc.*_ga_NEXN8H46L5*MTcxODI2MTY0Ni4xLjEuMTcxODI2MjkzMS4wLjAuMTcwNDA3OTI1MA

>Extract arduino-1.8.19-linuxaarch64.tar in Downloads directory

```
cd ~/Downloads
tar -xvf arduino-1.8.19-linuxaarch64.tar
cd ~/Downloads/arduino-1.8.19
sudo sh install.sh
```

>After connect arduino and Jetson nano, check connection
```
ls -l /dev/ttyACM0
```


>Authorize
```
sudo usermod -a -G dialout jetson
sudo chmod a+rw /dev/ttyACM0
```

>Install rosserial library
```
cd ~/catkin_ws/src/sea-me-hackathon-2024/ultrasonic_ros
arduino ultrasonic_ros.ino
```
![다운로드](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/ae8e9c9f-199f-4c23-8273-0b14bb9b94fd)
![4](https://github.com/AveesLab/sea-me-hackathon-2024/assets/117966644/04736dab-03c4-41ef-8e08-6f96812eacd4)

>Fix the code
```
cd ~/Arduino/libraries/Rosserial_Arduino_Library/src/ros
gedit msg.h
```
```
-- #include <cstring>
++ #include <string.h>
-- std::memcpy
++ memcpy
```

>Check the result
```
roscore
roslaunch usb_cam usb_cam-test.launch
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=9600
rosrun rosrun joy joy_node
rosrun control actuator
rosrun todo todo
```


>You can see this picture

![rqt_graph](https://github.com/AveesLab/sea-me-hackathon-2024/assets/78201406/a55781e3-d396-42e0-a811-7b0e72f5938b)

>>>>>>> 1a13bb8345cf2c917ba39a2854cb7734fb38a365