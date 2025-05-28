#include <stdio.h>
#include <wiringPi.h>


int main()
{

    wiringPiSetup();
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    digitalWrite(7, 1);

    return 0;
}