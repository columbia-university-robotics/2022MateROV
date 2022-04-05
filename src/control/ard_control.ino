#include <Servo.h>

// initialzing servo objects for each motor
Servo UD_left;
Servo UD_right;
Servo front_left;
Servo front_right;
Servo back_left;
Servo back_right;

// assigning a pin value to each motor
int UD_left_pin = 5;
int UD_right_pin = 6;
int front_right_pin = 7;
int front_left_pin = 8;
int back_right_pin = 9;
int back_left_pin = 10;

// setting the default value of the motors to be in the off position
int DEFAULT_OFF = 1500;

int motor1 = DEFAULT_OFF;
int motor2 = DEFAULT_OFF;
int motor3 = DEFAULT_OFF;
int motor4 = DEFAULT_OFF;
int motor5 = DEFAULT_OFF;
int motor6 = DEFAULT_OFF;

String input;

void setup() {
  Serial.begin(115200);
  
  UD_left.attach(UD_left_pin);
  UD_right.attach(UD_right_pin);
  front_left.attach(front_left_pin);
  front_right.attach(front_right_pin);
  back_left.attach(back_left_pin);
  back_right.attach(back_right_pin);

  UD_left.writeMicroseconds(motor1);
  UD_right.writeMicroseconds(motor2);
  front_left.writeMicroseconds(motor3);
  front_right.writeMicroseconds(motor4);
  back_left.writeMicroseconds(motor5);
  back_right.writeMicroseconds(motor6);
  
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  
  // reads in the input from the python code
  input = Serial.readString();

  // parses throught the string to get the respective integer values
  motor1 = input.substring(0, 4).toInt();
  motor2 = input.substring(5, 9).toInt();
  motor3 = input.substring(10, 14).toInt();
  motor4 = input.substring(15, 19).toInt();
  motor5 = input.substring(20, 24).toInt();
  motor6 = input.substring(25, 29).toInt();

  // writes the values to the motors
  UD_left.writeMicroseconds(motor1);
  UD_right.writeMicroseconds(motor2);
  front_left.writeMicroseconds(motor3);
  front_right.writeMicroseconds(motor4);
  back_left.writeMicroseconds(motor5);
  back_right.writeMicroseconds(motor6);
}
