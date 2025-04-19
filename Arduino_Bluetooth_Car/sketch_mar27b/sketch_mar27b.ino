// Motor driver pins
int in1 = 9, in2 = 8;
int in3 = 7, in4 = 6;
int ena = 3, enb = 11;

// IR Sensor Pins (Analog Inputs)
int sr = A2;  // Right Sensor (Analog)
int sl = A3;  // Left Sensor (Analog)

// Sensor Threshold (Adjust based on lighting)
int threshold = 336; 

// Speed configuration
int speedA = 150;  // Base speed for motor A
float speedB = 175.5;  // Base speed for motor B

void setup() {
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);
    pinMode(ena, OUTPUT);
    pinMode(enb, OUTPUT);

    Serial.begin(9600);
    delay(2000); // Initial delay before start
    analogWrite(ena, 0);
    analogWrite(enb, 0);
}

void loop() {
    // Read sensor values (Analog Read)
    int svr = analogRead(sr);
    int svl = analogRead(sl);

    // Convert to digital (Black = LOW, White = HIGH)
    bool right_black = (svr > threshold);  // Black = LOW
    bool left_black = (svl > threshold);

    // Debugging output
    Serial.print("Left Sensor: ");
    Serial.print(svl);
    Serial.print(" | Right Sensor: ");
    Serial.println(svr);

    // Decision Making
    if (left_black && right_black) {  // Stop (both on black)
        Serial.println("Stop");
        moveMotors(LOW, LOW, LOW, LOW, 0, 0);
    } 
    else if (left_black && !right_black) {  // Turn left
        Serial.println("Turning Left");
      moveMotors(LOW, HIGH, HIGH, LOW, speedA, speedB );
    }
    else if (!left_black && right_black) {  // Turn right
        Serial.println("Turning Right");
         
         moveMotors(HIGH, LOW, LOW, HIGH, speedA , speedB);
    } 
        
    
    else {  // Move forward
        Serial.println("Moving Forward");
        moveMotors(LOW, HIGH, LOW, HIGH, speedA, speedB);
    }
        delay(28);
        moveMotors(LOW, LOW, LOW, LOW, 0, 0);
   
  
    
}

// Function to control motor movements
void moveMotors(int in1State, int in2State, int in3State, int in4State, int speedA, int speedB) {
    digitalWrite(in1, in1State);
    digitalWrite(in2, in2State);
    digitalWrite(in3, in3State);
    digitalWrite(in4, in4State);
    analogWrite(ena, speedA);
    analogWrite(enb, speedB);
}
