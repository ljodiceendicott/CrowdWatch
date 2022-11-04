//const int buttonPin = 2;  // the number of the pushbutton pin
//const int ledPin = 13;    // the number of the LED pin
//
//
//// variables will change:
//int buttonState = 0;  // variable for reading the pushbutton status
//void setup() {
//  // initialize the pushbutton pin as an input:
//  pinMode(buttonPin, INPUT);
//  Serial.begin(9600);
//  Serial.setTimeout(1);
//  
//}
//
//void loop() {
//  buttonState = digitalRead(buttonPin);
//  // read the state of the pushbutton value:
//  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
//  if (buttonState == HIGH) {
//  Serial.println("high");
//    
////    digitalWrite(ledPin, HIGH);
//  }
////  if (buttonState == LOW){
////    Serial.println("nope");
////  }
// 
//
////  delay(2000);
//}

const int buttonPin = 2; 
int buttonState = 0;

void setup(){
   Serial.begin(9600);
   Serial.setTimeout(1);
  pinMode(buttonPin,INPUT);

}
void loop(){
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.write('h');
    delay(200);
  }
}
