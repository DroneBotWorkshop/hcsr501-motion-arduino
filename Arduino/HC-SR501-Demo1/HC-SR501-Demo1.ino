/*
  HC-SR501 Motion Sensor Demonstration 1
  HC-SR501-Demo1.ino
  Motion Sensor with Delay
  Set sensor for 3-second trigger
  DroneBot Workshop 2018
  https://dronebotworkshop.com
*/

// Define pins for LEDs
int detectedLED = 13;
int readyLED = 12;
int waitLED = 11;

// Input from Motion Sensor
int pirPin = 7;

// Variable for Motion Detected
int motionDetected = 0;

// Variable to store value from PIR
int pirValue;


void setup() {

  // Setup LEDs as Outputs
  pinMode(detectedLED, OUTPUT);
  pinMode(readyLED, OUTPUT);
  pinMode(waitLED, OUTPUT);

  // Setup PIR as Input
  pinMode(pirPin, INPUT);

  // Initial 1 Minute Delay to stabilize sensor
  digitalWrite(detectedLED, LOW);
  digitalWrite(readyLED, LOW);
  digitalWrite(waitLED, HIGH);
  delay(60000);
  digitalWrite(readyLED, HIGH);
  digitalWrite(waitLED, LOW);

}

void loop() {

  // Get value from motion sensor
  pirValue = digitalRead(pirPin); detectedPin
  // See if motion Detected
  if (pirValue == 1) {
    // Display Triggered LED for 3 seconds
    digitalWrite(detectedLED, HIGH);
    motionDetected = 1;
    delay(3000);
  } else {
    digitalWrite(detectedLED, LOW);
  }
  // Add delay after triggering to reset sensor
  if (motionDetected == 1) {
    // After trigger wait 6 seconds to re-arm
    digitalWrite(detectedLED, LOW);
    digitalWrite(readyLED, LOW);
    digitalWrite(waitLED, HIGH);
    delay(6000);
    digitalWrite(readyLED, HIGH);
    digitalWrite(waitLED, LOW);
    motionDetected = 0;
  }

}
