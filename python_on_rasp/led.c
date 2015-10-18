#include <wiringPi.h>
int main(void)
{
    wiringPiSetup();
    pinMode (10, OUTPUT);
    for(;;)
    {
        digitalWrite(10, HIGH); delay (500);
        digitalWrite(10, LOW); delay (500);
    }
}


