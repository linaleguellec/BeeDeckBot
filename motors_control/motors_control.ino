
/*
 * ce code fonctionne le 2 juin 2023 
 * sincronise la porte rfid et le robot fleur
 * chois des phase aleatoire 
 * sincronisation des phases et frequence pour allure de fleur
 */


#include <Arduino.h>
#include "DynamixelMotor.h"
#include <MatrixMath.h>
     
#define pi    3.1415926535897932384626433832795

long t_0, t_1, t;

int angle[2] = {1023/2, 1023/2};
int init_angle[2];

float r[2] = {5, 12.14};

float Ax_tab[] = {3.0, 5.0, 7.0};
float Az_tab[] = {1.0, 2.0, 3.0};
float fx_tab[] = {0.2, 0.3, 0.5};
float tau_tab[] = {0.0, 0.25, 0.5, 0.75, 1.0};

float f_z, f_x, A_z, A_x, phi_x, phi_z;
float tau;


const uint8_t id_z =1;
const uint8_t id_x =2;

int16_t spe=1023;
const long unsigned int baudrate = 1000000;

HardwareDynamixelInterface interface(Serial);

DynamixelMotor motor_z(interface, id_z);
DynamixelMotor motor_x(interface, id_x);

int etat = 0;
int trig = 0;
int trig_pin = 5;

int rfid_pin = 8;
int rfid_pin_val = 0; 
int rfid_pin_val_was = 0;

/*
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
*/
void setup()
{ 
  pinMode(trig_pin, INPUT);
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
  /*++++++++++++++++++++++++++++++++++++++++++++++++++*/
  pinMode(rfid_pin, INPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  /*++++++++++++++++++++++++++++++++++++++++++++++++++*/
  interface.begin(baudrate);
  delay(100);
  uint8_t status_x=motor_x.init();
  if(status_x!=DYN_STATUS_OK)
  {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH);
    while(1);
  }
  motor_z.enableTorque();  
  motor_z.jointMode(0, 1023);
  motor_z.speed(spe);
  
  motor_x.enableTorque();  
  motor_x.jointMode(0, 1023);
  motor_x.speed(spe);

  delay(200);
  init_phase();

  delay(1000);
  
  /*++++++++++++++++++++++++++++++++++++++++++++++++++*/
  t_0 = millis();
  /*++++++++++++++++++++++++++++++++++++++++++++++++++*/
 
}

/*
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
*/

 void init_phase(){

    int taille_Ax_tab = sizeof(Ax_tab)/sizeof(Ax_tab[0]);
    int taille_Az_tab = sizeof(Az_tab)/sizeof(Az_tab[0]);
    int taille_tau_tab = sizeof(tau_tab)/sizeof(tau_tab[0]);
    int taille_fx_tab = sizeof(fx_tab)/sizeof(fx_tab[0]);
  
    int index_Ax_tab = random(taille_Ax_tab);
    int index_Az_tab = random(taille_Az_tab);
    int index_tau_tab = random(taille_tau_tab);
    int index_fx_tab = random(taille_fx_tab);
    
    A_x = Ax_tab[index_Ax_tab];
    A_z = Az_tab[index_Az_tab];
    tau = tau_tab[index_tau_tab];
    f_x = fx_tab[index_fx_tab];

    f_z = 2*f_x;

    if ( tau < 0.25) {
      phi_x = (pi/2)*(1 - 4*tau);
      phi_z = (pi/2)*(8*tau - 1);
    }
  
    else if ( tau < 0.5) {
      phi_x = (pi/2)*(1 - 4*tau);
      phi_z = - (pi/2)*(8*(tau - 0.25) - 1);
    }
    
    else if ( tau < 0.75) {
      phi_x = - (pi/2)*(1 - 4*(tau - 0.5));
      phi_z = (pi/2)*(8*(tau - 0.5) - 1);
    }
    
    else {
      phi_x = - (pi/2)*(1 - 4*(tau - 0.5));
      phi_z = - (pi/2)*(8*(tau - 0.75) - 1);
    }
 
}
  


void Gestion(){
  
  rfid_pin_val_was = rfid_pin_val;
  rfid_pin_val = digitalRead(rfid_pin);
  
  switch(etat){

    case 0:
      if (rfid_pin_val == 1 and  rfid_pin_val_was == 0){
        etat = 1;
        delay(500);
        t_0 = millis();
      }
    break;
    
    case 1:
      if (rfid_pin_val == 1 and  rfid_pin_val_was == 0){
        etat = 0;
        init_phase();
        Serial.print("init phase");
        delay(500);
      }
    break;
    
  }
}

void Action(int etat){
   switch(etat){
    case 0:
      init_mov();
      motor_z.goalPosition(init_angle[0]);
      motor_x.goalPosition(init_angle[1]);
    break;

    case 1:
      gen_mov();
      motor_z.goalPosition(angle[0]);
      motor_x.goalPosition(angle[1]);
    break;
  }

  
}


void gen_mov(){
  
  float z_d =  sin((2.00*pi*f_z*(float)t/1000) + phi_z);
  z_d = 0.5*(z_d-1.00)*A_z;

  float x_d =  sin(2.00*pi*f_x*(float)t/1000 + phi_x);
  x_d = 0.5*(x_d)*A_x;

  float a_z = atan((z_d/r[0]))*(180/pi);
  float a_x = atan((x_d/r[1]))*(180/pi);
  
  angle[0] = (int)((1023/2) + (a_z*1023/300));
  angle[1] = (int)((1023/2) + (a_x*1023/300));
  
}

void init_mov(){
  
  float z_d =  sin(phi_z);
  z_d = 0.5*(z_d-1.00)*A_z;

  float x_d =  sin(phi_x);
  x_d = 0.5*(x_d)*A_x;

  float a_z = atan((z_d/r[0]))*(180/pi);
  float a_x = atan((x_d/r[1]))*(180/pi);
  
  init_angle[0] = (int)((1023/2) + (a_z*1023/300));
  init_angle[1] = (int)((1023/2) + (a_x*1023/300));
  
}

/*
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
*/

void loop() 
{
  t_1 = millis();
  t = (t_1-t_0); 
  Gestion();
  Action(etat);

}
