import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
from conn_dataBase import *
import psycopg2
import datetime
import subprocess

# conexión base de datos
host = "192.168.50.252"
database = "monitor_invernadero"
port = "5432"
user = "Administrador"
password = "1234"

conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
cur = conn.cursor()

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()

tabla = 'invernadero_1'

while True:
    try:
        fecha_actual = datetime.datetime.now()
        while not radio.available(0):
            time.sleep(0.01)
        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
        # print("Received: {}".format(receivedMessage))
        print("Recibiendo los datos de Humedad, Temperatura y Humedad del suelo...")
        string = ""
        for n in receivedMessage:
            if (n >= 32 and n <= 126):
                string += chr(n)
        print(string)
        hum = string[0:5]
        temp = string[5:10]
        hum_suelo = string[10:14]
        print(hum)
        print(temp)
        print(hum_suelo)
        insert_query = f"INSERT INTO {tabla} (invernadero_id, temperatura, humedad_suelo, plantas_id, humedad, last_update) VALUES (%s, %s, %s, %s, %s,CURRENT_TIMESTAMP);"
        cur.execute(insert_query, ('1', temp, hum_suelo, '1', hum))
        conn.commit()
        time.sleep(4)
    except KeyboardInterrupt:
        cur.close()
        conn.close()
        GPIO.cleanup()
        break
