//Incluir librerias
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include "DHT.h"
#define DHTTYPE DHT11
//crear un objeto RF24
RF24 radio(9, 8);  // CE, CSN
//Para los sensores
const int DHTPin = 7; // Pin digital
DHT dht(DHTPin, DHTTYPE);
unsigned long previousMillis = 0;
long interval = 2000;
// Sensor de humedad de suelo
#define suelo A1 // Se define pin analogo de lectura
int hum_suelo;
// Sensor de nivel de agua
#define nivel A2
int nivel_agua;
// Leds nivel de agua
const int led1 = 4;
const int led2 = 5;
const int led3 = 6;
// bomba de agua
const int bomba=8;
//Lectura de datos
unsigned long previoMill = 0;
char mensaje[] = "";
void setup()
{
  //Para los sensores
  Serial.begin(9600);
  dht.begin();
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(bomba,OUTPUT);  
  //Para enviar los datos por RF
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.enableAckPayload();
  radio.powerUp();
  //ajusta el módulo como transmisor
  radio.stopListening();
}
void loop()
{
  unsigned long currentMillis = millis();
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();
  if ((currentMillis - previousMillis)>=interval){
    previousMillis = currentMillis;  
    if (isnan(hum) || isnan(temp)) {
      return;
    }
    hum_suelo = analogRead(suelo);
    nivel_agua = analogRead(nivel);
  }
  if (nivel_agua < 500 ){
    digitalWrite(led3,HIGH);
    digitalWrite(led1,LOW);
    digitalWrite(led2,LOW);
  }else if(nivel_agua < 600){
    digitalWrite(led2,HIGH);
    digitalWrite(led3,LOW);
    digitalWrite(led1,LOW);
  }else{
    digitalWrite(led1,HIGH);
    digitalWrite(led3,LOW);
    digitalWrite(led2,LOW);
  }
  delay(100);
  if (hum_suelo<300){
    digitalWrite(bomba,HIGH);
  }else{
    digitalWrite(bomba,LOW);
  }
  if ((currentMillis - previoMill)>=3000){
    Serial.print(hum);
    Serial.print(temp);
    Serial.println(hum_suelo);
    String data = String(hum) + String(temp) + String(hum_suelo);
    const char* text = data.c_str();
    radio.write(text, strlen(text));
  }
}