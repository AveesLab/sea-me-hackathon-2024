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
