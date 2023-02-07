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
const int buttonCycleLeftPin = 3;
const int buttonCycleRightPin = 2;
const int buttonincrease = 4;
const int buttondecrease = 5;

int locnum = 0;
String phrase;  

void setup(){
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(buttonCycleLeftPin, INPUT);
  pinMode(buttonCycleRightPin, INPUT);
  pinMode(buttonincrease, INPUT);
  pinMode(buttondecrease, INPUT);

}
void loop(){
  if(Serial.avaliable()){
    phrase = Serial.readStringUntil('\n')
    if(phrase.equals("start")){
      // read in first location, name followed by count
      // firstContact();
    }
    else{
      // read for change
      if(digitalRead(buttonCycleLeftPin)== HIGH){
        // shift current location being tracked by -1
      }
      else if(digitalRead(buttonCycleRightPin)== HIGH){
        // shift current location being tracked by +1
      }
      if(digitalRead(buttonIncrease)== HIGH){
        // increase current count by one
      }
      else if(digitalRead(buttonDecrease)==HIGH){
        // decrease current count by one
      }
    }
  }

  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.write('h');
    delay(200);
  }
}
