#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define SERVO   29

int main(int n, char **s) // arg로 servo 모터의 회전각도를 입력받는다다
{

    if(n < 2)
    {
        printf("usage : servo [Rotate degree (0 ~ 180)]\n");
        return 0;
    }

    wiringPiSetup();
    pinMode(SERVO, OUTPUT);

    // HIGH 1000 == 90도
    //      2000 == 180도?
    int r = (atoi(s[1]) * 500) / 90;

    for(int i = 0; i<200; i++)
    {
        digitalWrite(SERVO, HIGH);
        delayMicroseconds(r);
        digitalWrite(SERVO, LOW);
        delayMicroseconds(20000-r);
    }
    
    
    

    return 0;
}