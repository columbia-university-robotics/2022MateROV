#include <Servo.h>

String s;
int timeout = 0;
int f1 = 1500;
int f2 = 1500;
int f3 = 1500;
int f4 = 1500;
int f5 = 1500;
int f6 = 1500;
Servo m1;
Servo m2;
Servo m3;
Servo m4;
Servo m5;
Servo m6;
int motorCount;

void setup() {
  Serial.begin(9600);
  m1.attach(8);
  m2.attach(9);
  m3.attach(10);
  m4.attach(11);
  m5.attach(12);
  m6.attach(13);
  m1.writeMicroseconds(1500);
  m2.writeMicroseconds(1500);
  m3.writeMicroseconds(1500);
  m4.writeMicroseconds(1500);
  m5.writeMicroseconds(1500);
  m6.writeMicroseconds(1500);

  delay(7000);

}

void loop() {
  if (Serial.available() > 0) {
    timeout = 0;
    s = Serial.readStringUntil('/'); //strings should be comma separated float values (including last one). String ends with '/'.
    motorCount = 0;
    int left = 0;
    int right = 0;
    float readValue = 0;

    for(int i = 0; i < s.length(); i++){
      if(s[right] == ','){
        motorCount++;
        readValue = (s.substring(left,right).toFloat());
        left = right + 1;
        int pwmVal = map(int(readValue*100), -100, 100, 1100, 1900); //need to go from float to int, unfortunately
        if(motorCount == 1){
          m1.writeMicroseconds(pwmVal);
          f1 = pwmVal;
        }
        if(motorCount == 2){
          m2.writeMicroseconds(pwmVal);
          f2 = pwmVal;
        }
        if(motorCount == 3){
          m3.writeMicroseconds(pwmVal);
          f3 = pwmVal;
        }
        if(motorCount == 4){
          m4.writeMicroseconds(pwmVal);
          f4 = pwmVal;
        }
        if(motorCount == 5){
          m5.writeMicroseconds(pwmVal);
          f5 = pwmVal;
        }
        if(motorCount == 6){
          m6.writeMicroseconds(pwmVal);
          f6 = pwmVal;
        }
      }
      right++;
    }
    
  }
  else{
    timeout++;
    if(timeout > 500){
      f1 = 0;
      f2 = 0;
      f3 = 0;
      f4 = 0;
      f5 = 0;
      f6 = 0;
    }
    m1.writeMicroseconds(f1);
    m2.writeMicroseconds(f2);
    m3.writeMicroseconds(f3);
    m4.writeMicroseconds(f4);
    m5.writeMicroseconds(f5);
    m6.writeMicroseconds(f6);
  }

  delay(1);

}
