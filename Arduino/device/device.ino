#include <LiquidCrystal.h>
const int buttonCycleLeftPin = 7;
const int buttonCycleRightPin = 8;
const int buttonIncrease = 9;
const int buttonDecrease = 13;

String locs[20] = {"Men's Clothing Section", "Women's Clothing Section", "Electronics Section", "Shoe Section", "Toy Section", "Home Decor Section", "Pet Supplies Section", "Beauty and Personal Care Section", "Jewelry Section", "Sporting Goods Section", "Baby Products Section", "Kitchen and Dining Section", "Appliances Section", "Food and Beverage Section", "Health and Wellness Section", "Outdoor and Garden Section", "Furniture Section", "Entertainment Section", "Home Improvement Section", "Office Supplies Section"};

int count[20] = {12, 10, 8, 15, 20, 7, 6, 9, 6, 9, 7, 10, 8, 12, 11, 6, 13, 8, 11, 14};

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int cycleLeftButtonState, cycleRightButtonState = 0;
int increaseButtonState, decreaseButtonState = 0;

int locnum = 0;
String phrase;
bool write = false;

void setup()
{
  Serial.begin(19200);
  Serial.setTimeout(1);

  lcd.begin(16, 2);

  pinMode(buttonCycleLeftPin, INPUT);
  pinMode(buttonCycleRightPin, INPUT);
  pinMode(buttonIncrease, INPUT);
  pinMode(buttonDecrease, INPUT);
}
void loop()
{
  // lcd.print("ITS NOT A BOMB");
  // if(!write){
  //   lcd.print(myArray[locnum]);
  //   write = true;
  // }
  lcd.print("   " + locs[locnum]);
  lcd.setCursor(0, 1);
  lcd.println("Count:     ");
  lcd.print(count[locnum]);

  // delay(500);
  // lcd.clear();
  // delay(500);

  cycleLeftButtonState = digitalRead(buttonCycleLeftPin);
  cycleRightButtonState = digitalRead(buttonCycleRightPin);
  if (cycleLeftButtonState == HIGH)
  {
    Serial.println('<');
    locnum = locnum + 1;
    lcd.clear();
    delay(1000); // Delay to stop double inputs unless they are intentional
  }
  if (cycleRightButtonState == HIGH)
  {
    Serial.println('>');
    locnum = locnum - 1;
    lcd.clear();
    delay(1000);
  }
  increaseButtonState = digitalRead(buttonIncrease);
  decreaseButtonState = digitalRead(buttonDecrease);
  if (increaseButtonState == HIGH)
  {
    Serial.println('+');
    count[locnum] = count[locnum] + 1;
    lcd.clear();
    delay(500); // Delay to stop double inputs unless they are intentional
  }
  if (decreaseButtonState == HIGH)
  {
    Serial.println('-');
    count[locnum] = count[locnum] - 1;
    lcd.clear();
    delay(1000);
  }


}
