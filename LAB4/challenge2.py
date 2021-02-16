#include <U8g2lib.h>
#include <U8x8lib.h>
const int accelX = A0;

int streaks = 0;
int counter = 0;

void setup()
{
    setupDisplay();
    Serial.begin(9600);
    pinMode(accelX, INPUT);
}
void loop()
{
  int accel_val = analogRead(accelX);
  counter += 1;
    Serial.println(accel_val); 
    if (accel_val >= 2100) { 
          streaks = 1;

    }
    if (accel_val <= 2100) {
      counter += 1;
    }
    
    if (counter >= 2000) { //countdown checker
        
        streaks = 0;
        counter = 0;
      }  
    if (streaks == 1) {
      writeDisplay("Keep it up!", 0, true);
    }
    if (streaks == 0) {
      writeDisplay("Get moving!", 0, true);
    }
    
    
}
