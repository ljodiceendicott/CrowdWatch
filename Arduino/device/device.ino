#include <LiquidCrystal.h>
const int buttonCycleLeftPin = 7;
const int buttonCycleRightPin = 10;
const int buttonIncrease = 9;
const int buttonDecrease = 13;

int myArray[10]={9, 3, 2, 4, 3, 2, 7, 8, 9, 11};

LiquidCrystal lcd(12,11,5,4,3,2);

int cycleLeftButtonState,cycleRightButtonState = 0;
int increaseButtonState, decreaseButtonState = 0;

int locnum = 0;
String phrase;  
bool write= false;

void setup(){
  Serial.begin(19200);
  Serial.setTimeout(1);

  lcd.begin(16,2);

  pinMode(buttonCycleLeftPin, INPUT);
  pinMode(buttonCycleRightPin, INPUT);
  pinMode(buttonIncrease, INPUT);
  pinMode(buttonDecrease, INPUT);

}
void loop(){
  // lcd.print("ITS NOT A BOMB");
  // if(!write){
  //   lcd.print(myArray[locnum]);
  //   write = true;
  // }
  lcd.print("Test Location");
  lcd.setCursor(0, 1);
  lcd.print("Count: alot     ");
  // delay(500);
  // lcd.clear();
  // delay(500);
    
  cycleLeftButtonState = digitalRead(buttonCycleLeftPin);
  cycleRightButtonState = digitalRead(buttonCycleRightPin);
  if(cycleLeftButtonState == HIGH){
    Serial.println('<');
    locnum = locnum +1;
    delay(1000);//Delay to stop double inputs unless they are intentional
  }
  if(cycleRightButtonState == HIGH){
    Serial.println('>');
    locnum = locnum-1;
    delay(1000);
  }
increaseButtonState = digitalRead(buttonIncrease);
decreaseButtonState = digitalRead(buttonDecrease);
  if(increaseButtonState == HIGH){
    Serial.println('+');
    delay(500);//Delay to stop double inputs unless they are intentional
  }
  if(decreaseButtonState == HIGH){
    Serial.println('-');
    delay(1000);
  }


  // if(Serial.avaliable()){
  //   phrase = Serial.readStringUntil('\n')
  //   if(phrase.equals("start")){
  //     // read in first location, name followed by count
  //     // firstContact();
  //   }
  //   else{
  //     // read for change
  //     if(digitalRead(buttonCycleLeftPin)== HIGH){
  //       // shift current location being tracked by -1
  //     }
  //     else if(digitalRead(buttonCycleRightPin)== HIGH){
  //       // shift current location being tracked by +1
  //     }
  //     if(digitalRead(buttonIncrease)== HIGH){
  //       // increase current count by one
  //     }
  //     else if(digitalRead(buttonDecrease)==HIGH){
  //       // decrease current count by one
  //     }
  //   }
  // }

  // buttonState = digitalRead(buttonPin);
  // if (buttonState == HIGH) {
  //   Serial.write('h');
  //   delay(200);
  // }
  



}
