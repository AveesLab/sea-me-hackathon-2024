#define TRIG 9
#define ECHO 8

#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle nh;
std_msgs::Float32 distance_;
ros::Publisher distancePublisher("/distance", &distance_);

void setup()
{
  nh.initNode();
  nh.advertise(distancePublisher);
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop()
{
  float duration, distance;
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn (ECHO, HIGH);
  distance = duration * 17 / 1000;
  
  Serial.println(duration);
  Serial.print("\nDIstance : ");
  Serial.print(distance);
  Serial.println(" Cm");
  
  distance_.data = distance;
  distancePublisher.publish(&distance_);
  nh.spinOnce();
  delay(100);
}
