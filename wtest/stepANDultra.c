#include <stdio.h>
#include <wiringPi.h>

#define ORANGE  21
#define YELLOW  22
#define PINK    23
#define BLUE    24

#define TRIG    27
#define ECHO    28

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

void Trigger()
{
    //Trigger signal
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);
    delayMicroseconds(200); //wait for Burst signal end

}

double Distance()
{
    while(1)    //Burst over(finish), count start
    {
        int e =    digitalRead(ECHO);
        if(e == 1) break;
    }
    int t1=micros();
    while(1)    //wait until echo receive 
    {
        int e=digitalRead(ECHO);
        if(e==0) break;
    }
    int t2=micros();

    double dist = (t2-t1)*.017;

    return dist;
}

int main()
{
    wiringPiSetup();
    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);
    pinMode(ORANGE, OUTPUT);
    pinMode(YELLOW, OUTPUT);
    pinMode(PINK, OUTPUT);
    pinMode(BLUE, OUTPUT);

    digitalWrite(TRIG, LOW); delay(10); //initial pin status 0

    int wave_index = 0;
    int distcheck_count = 0;
    double dist = 0;


    while(1)
    {
        distcheck_count++;

        if(distcheck_count > 40)
        {
            distcheck_count=0;
            //Trigger signal
            Trigger();
            dist = Distance();
            printf("Distance : %.2fcm\n\n", dist);
        }


        if(dist < 50)
        {
            wave_index++;
            wave_index%=4;
            step_wave(wave_index);
        }else{
            wave_index--;
            wave_index = (wave_index+4)%4;
            step_wave(wave_index);
        }

        delay(5);
        
    }

    return 0;

}