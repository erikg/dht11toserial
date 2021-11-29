#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

#define DHT_PIN 11

DHT dht(DHT_PIN, DHT11);

void setup() {
	Serial.begin(9600);
	dht.begin();
}

void printTemp(float temp, float hum) {
	Serial.print("{\"TEMP\":");
	Serial.print(temp);
	Serial.print(",\"HUM\":");
	Serial.print(hum);
	Serial.println("}");
}

void loop() {
	float temp, hum;
	dht.read(true);
	delay(10);
	temp = dht.readTemperature();
	hum = dht.readHumidity();
	printTemp(temp, hum);
	delay(5000);
}
