//const int buttonPin = 2;  // the number of the pushbutton pin
//const int ledPin = 13;    // the number of the LED pin
//const int otherButtonPin = 6;
//
//// variables will change:
//int buttonState = 0;  // variable for reading the pushbutton status
//int otherbuttonstate = 0;
//
//void setup() {
//  // initialize the LED pin as an output:
////  pinMode(ledPin, OUTPUT);
//  // initialize the pushbutton pin as an input:
//  pinMode(buttonPin, INPUT);
//  pinMode(otherButtonPin, INPUT);
//
//  Serial.begin(9600);
//  Serial.setTimeout(1);
//}
//
//void loop() {
//  // read the state of the pushbutton value:
//Serial.println("ok");
//
//exit(1);
//}

const int buttonPin = 2;  // the number of the pushbutton pin
const int ledPin = 13;    // the number of the LED pin

// variables will change:
int buttonState = 0;  // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    Serial.println('H');
//    digitalWrite(ledPin, HIGH);
  } else {
    // turn LED off:
   Serial.println('L');
//    digitalWrite(ledPin, LOW);
  }

//  delay(2000);
}
