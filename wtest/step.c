#include <stdio.h>
#include <wiringPi.h>

#define ORANGE  21
#define YELLOW  22
#define PINK    23
#define BLUE    24
#define RED     25 // VCC로 활용하려고 했지만 전압이 약해서 실패,,

void step_wave(int step)
{
    switch(step){
        case 0:
            digitalWrite(ORANGE,    1);
            digitalWrite(YELLOW,    0);
            digitalWrite(PINK,      0);
            digitalWrite(BLUE,      0);
            break;
        case 1:
            digitalWrite(ORANGE,    0);
            digitalWrite(YELLOW,    1);
            digitalWrite(PINK,      0);
            digitalWrite(BLUE,      0);
            break;
        case 2:
            digitalWrite(ORANGE,    0);
            digitalWrite(YELLOW,    0);
            digitalWrite(PINK,      1);
            digitalWrite(BLUE,      0);
            break;
        case 3:
            digitalWrite(ORANGE,    0);
            digitalWrite(YELLOW,    0);
            digitalWrite(PINK,      0);
            digitalWrite(BLUE,      1);
            break;
    }
}

void step_full(int step)
{
    switch(step){
        case 0:
            digitalWrite(ORANGE,    1);
            digitalWrite(YELLOW,    1);
            digitalWrite(PINK,      0);
            digitalWrite(BLUE,      0);
            break;
        case 1:
            digitalWrite(ORANGE,    0);
            digitalWrite(YELLOW,    1);
            digitalWrite(PINK,      1);
            digitalWrite(BLUE,      0);
            break;
        case 2:
            digitalWrite(ORANGE,    0);
            digitalWrite(YELLOW,    0);
            digitalWrite(PINK,      1);
            digitalWrite(BLUE,      1);
            break;
        case 3:
            digitalWrite(ORANGE,    1);
            digitalWrite(YELLOW,    0);
            digitalWrite(PINK,      0);
            digitalWrite(BLUE,      1);
            break;
    }
}

void step_half(int step)
{

}

int main()
{

    wiringPiSetup();
    pinMode(ORANGE, OUTPUT);
    pinMode(YELLOW, OUTPUT);
    pinMode(PINK, OUTPUT);
    pinMode(BLUE, OUTPUT);
    pinMode(RED, OUTPUT);
    digitalWrite(RED, HIGH);

    for(int i = 0; i<2048; i++)
    {
        step_wave(i % 4);
        delay(5);
    }

    return 0;
}