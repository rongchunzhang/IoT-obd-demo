#include <stdio.h>
#include <stdlib.h>
#include <softPwm.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>
#include <wiringPi.h>
#define Trig	28
#define Echo	29
#define BUFSIZE 512
void ultraInit(void)
{
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);
}

float disMeasure(void)
{
  struct timeval tv1;
  struct timeval tv2;
  long start, stop;
  float dis;

  digitalWrite(Trig, LOW);
  delayMicroseconds(2);

  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);	  //��������������
  digitalWrite(Trig, LOW);
  
  while(!(digitalRead(Echo) == 1));
  gettimeofday(&tv1, NULL);		   //��ȡ��ǰʱ��

  while(!(digitalRead(Echo) == 0));
  gettimeofday(&tv2, NULL);		   //��ȡ��ǰʱ��

  start = tv1.tv_sec * 1000000 + tv1.tv_usec;   //΢�뼶��ʱ��
  stop  = tv2.tv_sec * 1000000 + tv2.tv_usec;

  dis = (float)(stop - start) / 1000000 * 34000 / 2;  //�������

  return dis;
}
void run()     // ǰ��
{
    softPwmWrite(4,0); //����ǰ��
	softPwmWrite(1,250); 
	softPwmWrite(6,0); //����ǰ��
	softPwmWrite(5,250); 

 
}

void brake(int time)         //ɲ����ͣ��
{
    softPwmWrite(1,0); //����stop
	softPwmWrite(4,0); 
	softPwmWrite(5,0); //stop
	softPwmWrite(6,0); 
    delay(time * 100);//ִ��ʱ�䣬���Ե���  
}

void left(int time)         //��ת(���ֲ���������ǰ��)
{
    softPwmWrite(1,0); //����stop
	softPwmWrite(4,0); 
	softPwmWrite(5,0); //����ǰ��
	softPwmWrite(6,250); 
	delay(time * 300);
}



void right(int time)        //��ת(���ֲ���������ǰ��)
{
    softPwmWrite(1,0); //����ǰ��
	softPwmWrite(4,250); 
	softPwmWrite(5,0); //����stop
	softPwmWrite(6,0); 
    delay(time * 300);	//ִ��ʱ�䣬���Ե���  
}



void back(int time)          //����
{
    softPwmWrite(4,250); //����back
	softPwmWrite(1,0); 
	softPwmWrite(6,250); //����back
  	softPwmWrite(5,0); 
    delay(time *200);     //ִ��ʱ�䣬���Ե���  
}
int main(int argc, char *argv[])
{

    float dis;

   // char buf[BUFSIZE]={0xff,0x00,0x00,0x00,0xff};


    /*RPI*/
    wiringPiSetup();
    /*WiringPi GPIO*/
    pinMode (1, OUTPUT);	//IN1
    pinMode (4, OUTPUT);	//IN2
    pinMode (5, OUTPUT);	//IN3
    pinMode (6, OUTPUT);	//IN4
    softPwmCreate(1,1,500);   
    softPwmCreate(4,1,500);
    softPwmCreate(5,1,500);
    softPwmCreate(6,1,500);
  while(1){
    dis = disMeasure();
    printf("distance = %0.2f cm\n",dis);//�����ǰ��������õľ���
     if(dis<30){   //���ǰ���ϰ��ľ���С��30cmʱ����������Ӧ


	   back(4);//����500ms
	   left(4);//��ת300ms
	   

      }
     else {

        run();  //���ϰ�ʱǰ��
         }
  }
  return 0;

}

