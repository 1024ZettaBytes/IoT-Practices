# Practica ESP32
# Equipo:
# Jes煤s Eduardo Ram铆rez Cota. Ariel Aramburo Barraza, Carlos Eduardo Ruiz Parra
from machine import TouchPad, Pin
import network
import urequests
from time import sleep
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'INFINITUM5105_2.4'
password = 'ouKVi0FAfv'

api_key = '9mtvAMZjdagoKV08WksoItiC7DgAi31ooznOuaxQ8s'

station = network.WLAN(network.STA_IF)

station.active(True)
print('[*] Conectando a la red Wi-fi...')
station.connect(ssid, password)

while station.isconnected() == False:
  pass

# Hasta que se conecta a la red wifi llega aqu铆
print('[*] Se ha conectado a la red!')
print(station.ifconfig())

try:
  
  touch_pin = TouchPad(Pin(4))
  led =Pin(2, Pin.OUT)
  print('[*] Esperando para detectar contacto...')
  while True:
    touch_value = touch_pin.read()
    led.value(touch_value < 500)
    if touch_value <500:
      break
    sleep(0.5)
  temp = 25.3
  hum = 20.0
  pres = 18.3
  sensor_readings = {'value1':temp, 'value2':hum, 'value3':pres}
  print('[*] Lecturas del sensor:')
  print(sensor_readings)

  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    'https://maker.ifttt.com/trigger/pin_touched/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  print('[*] Request:')
  print(request.text)
  request.close()
  

except OSError as e:
  print('ERROR: Error al tratar de enviar los datos..')


