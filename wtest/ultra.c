#include <stdio.h>
#include <wiringPi.h>


#define TRIG    27
#define ECHO    28

int main()
{
    wiringPiSetup();
    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);

    digitalWrite(TRIG, LOW); delay(10); //initial pin status 0

    //Trigger signal
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);
    delayMicroseconds(200); //wait for Burst signal end


    return 1;

}