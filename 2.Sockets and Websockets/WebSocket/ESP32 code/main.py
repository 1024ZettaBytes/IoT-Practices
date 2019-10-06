# Practica ESP32
# Equipo:
# Jes煤s Eduardo Ram铆rez Cota. Ariel Aramburo Barraza, Carlos Eduardo Ruiz Parra
from machine import TouchPad, Pin
import network
import cliente
import os
from time import sleep
import esp
esp.osdebug(None)
import gc

gc.collect()

ssid = 'INFINITUM5105_2.4'
password = 'ouKVi0FAfV'
station = network.WLAN(network.STA_IF)
station.active(True)
print('[*] Conectando a la red Wi-fi...')
station.connect(ssid, password)

while station.isconnected() == False:
  pass

# Hasta que se conecta a la red wifi llega aqu铆
print('[*] Se ha conectado a la red!')
print(station.ifconfig())


touch_pin = TouchPad(Pin(4))
led =Pin(2, Pin.OUT)
print('[*] Esperando para detectar contacto...')
while True:
  touch_value = touch_pin.read()
  led.value(touch_value < 500)
  if touch_value <500:
    break
  sleep(0.5)
  
print('[*] Conectando al websocket...')
websocket = cliente.connect("ws://192.168.1.66:999/wsESP32")
print('[*] Se ha conectado al websocket!')
print('[*] Enviando información...')
websocket.send("Hola websocket! Soy ESP32 :)")
print('[*] Información enviada!')
websocket.close()
print('[*] Conexión terminada!')






