# Introduction to Arduino 

## Overview

This workshop is designed to introduce attendees to the basics of Arduino, its platform, and its applications in real-world scenarios. By the end of this workshop, participants will have a fundamental understanding of Arduino hardware and software, and will have hands-on experience with creating basic circuits and coding for Arduino.

# Schedule

<!-- # Chapter 1: Introduction to Arduino and Setup &nbsp; <img src="image\arduino-logo.png" alt="Arduino Uno Board" width="40"/> -->
# Chapter 1: Introduction to Arduino and Setup &nbsp; <img src="https://brandslogos.com/wp-content/uploads/images/arduino-logo-1.png" alt="Alt text" width="40"/>

- Introduction to Arduino
- Understanding the Arduino board and its components
- Installing the Arduino IDE (Integrated Development Environment)
- Setting up the Arduino board

# Chapter 2: Basic Electronics and Circuits

- Introduction to basic electronics (Voltage, Current, Resistance)
- Understanding basic components (Resistors, Capacitors, LEDs)
- Building simple circuits on a breadboard
- Reading schematics and understanding circuit diagrams

### Code Example: Blinking LED

```arduino
void setup() 
{
  pinMode(13, OUTPUT);  // Initialize the digital pin 13 as an output.
}

void loop() {
  digitalWrite(13, HIGH);  // Turn the LED on
  delay(1000);             // Wait for a second
  digitalWrite(13, LOW);   // Turn the LED off
  delay(1000);             // Wait for a second
}
```

### Code Example: Reading a Potentiometer

```arduino
void setup() {
  pinMode(13, OUTPUT);  // Initialize the digital pin 13 as an output.
}

void loop() {
  digitalWrite(13, HIGH);  // Turn the LED on
  delay(1000);             // Wait for a second
  digitalWrite(13, LOW);   // Turn the LED off
  delay(1000);             // Wait for a second
}
```


# Chapter 3: Programming the Arduino

- Introduction to Arduino programming
- Understanding the structure of an Arduino program
- Writing, compiling, and uploading a program to the Arduino board
- Debugging common errors


#### Example 1: Using &nbsp; `if` &nbsp; and &nbsp; `else` &nbsp;to control LED
```arduino
const int buttonPin = 2;  
const int ledPin = 13;    

void setup() {
  pinMode(buttonPin, INPUT);  
  pinMode(ledPin, OUTPUT);    
}

void loop() {
  int buttonState = digitalRead(buttonPin);  

  if(buttonState == HIGH) {  
    digitalWrite(ledPin, HIGH);  
  } else {
    digitalWrite(ledPin, LOW);   
  }
}
```

#### Example 2: Using for loop to blink LED multiple times
```arduino
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);    
}

void loop() {
  for(int i = 0; i < 5; i++) {  // Blink LED 5 times
    digitalWrite(ledPin, HIGH);  
    delay(500);                 
    digitalWrite(ledPin, LOW);   
    delay(500);                 
  }
  delay(2000);  // Wait for 2 seconds before blinking again
}

```

#### Example 3:  Using switch...case to control LED with different button presses
```arduino
const int buttonPin = 2;  
const int ledPin = 13;    

void setup() {
  pinMode(buttonPin, INPUT);  
  pinMode(ledPin, OUTPUT);    
}

void loop() {
  int buttonState = digitalRead(buttonPin);  

  switch(buttonState) {
    case HIGH:
      digitalWrite(ledPin, HIGH);  
      break;
    case LOW:
    default:
      digitalWrite(ledPin, LOW);   
      break;
  }
}

```
## In the examples provided above, participants can learn the following :

 - Using if and else to check the status of a button and control an LED.
 - Using a for loop to repeat the blinking of an LED multiple times.
 - Using switch...case to check the status of a button and control an LED.

## Materials Needed

- Arduino boards (1 per participant)
- USB cables (1 per participant)
- Breadboards
- Basic electronic components (Resistors, Capacitors, LEDs)
- Computers with the Arduino IDE installed

## Additional Resources

- [Arduino Official Website](https://www.arduino.cc/)
- [Arduino IDE Download](https://www.arduino.cc/en/Main/Software)
- [Basic Electronics Tutorials](https://www.electronics-tutorials.ws/)
- [Arduino Project Hub](https://create.arduino.cc/projecthub)

## Assessment

Participants will be assessed based on their understanding of the concepts, their ability to build circuits, and program the Arduino. A certificate of completion will be provided to all the participants who successfully complete the workshop.


# Chapter 4: Controlling Servo Motors

Servo motors are a type of motor that can be directed to rotate to particular positions, making them highly useful in robotics and other applications requiring precise control of motion. In this chapter, we will explore how to control a servo motor using an Arduino board.

## Overview

- Introduction to servo motors
- Working principle of servo motors
- Connecting a servo motor to Arduino
- Programming Arduino to control a servo motor

### Introduction to Servo Motors

Servo motors are different from the typical DC or stepper motors. They can rotate to specific angles based on the input signal they receive. A typical servo motor can rotate 180 degrees although some can rotate more or less than this.

### Working Principle of Servo Motors

The position of a servo motor is controlled by sending a pulse width modulated (PWM) signal through the control wire. The length of the pulse will determine how far the motor turns.

### Connecting a Servo Motor to Arduino

#### Materials Needed:
- Servo motor
- Jumper wires
- Breadboard

#### Connection Steps:

1. Connect the servo motor to the breadboard.
2. Connect the power wire (usually red) of the servo motor to the 5V pin on the Arduino.
3. Connect the ground wire (usually brown) of the servo motor to one of the GND pins on the Arduino.
4. Connect the control wire (usually orange or yellow) of the servo motor to one of the PWM pins on the Arduino (e.g., pin 9).

### Servo Motor Coneection Diagram
<!-- <img src="image\servo-motor-with-arduino-uno-wiring-diagram-schematic-circuit-tutorial.png" alt="Arduino Uno Board" width="600"/> -->
<img src="https://www.makerguides.com/wp-content/uploads/2020/08/servo-motor-with-arduino-uno-wiring-diagram-schematic-circuit-tutorial-featured-image-728x410.png" alt="Arduino Uno Board" width="600"/>




Arduino provides a `Servo` library which makes it easy to control a servo motor. Here is a simple example to sweep the servo motor from 0 to 180 degrees and back.

```arduino
#include <Servo.h>

Servo myservo;  // Create servo object to control a servo

void setup() {
  myservo.attach(9);  // Attaches the servo on pin 9 to the servo object
}

void loop() {
  for (int pos = 0; pos <= 180; pos += 1) { // Goes from 0 degrees to 180 degrees
    myservo.write(pos);                     // Tell servo to go to position in variable 'pos'
    delay(15);                              // Waits 15 milliseconds at each position
  }
  for (int pos = 180; pos >= 0; pos -= 1) { // Goes from 180 degrees to 0 degrees
    myservo.write(pos);                     // Tell servo to go to position in variable 'pos'
    delay(15);                              // Waits 15 milliseconds at each position
  }
}
```



## Additional Resources

- [Servo motor with Arduino](https://www.makerguides.com/servo-arduino-tutorial/)



---

**Note** : This is a simple outline and can be tailored according to the specific requirements and level of the attendees. Additional topics, projects, and resources can be included to extend the workshop or provide more in-depth coverage on certain topics.