from wifi_lib import conecta
import dht
import machine
import time
import urequests

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

print("Conectando...")
station = conecta(" ", " ")

WRITE_API_KEY = " "

d.measure()
payload = "&field1={}&field2={}".format(d.temperature(), d.humidity())

def conectData():
    resposta = urequests.post("https://api.thingspeak.com/update?api_key=" + WRITE_API_KEY + payload)
    resposta.close()
    
    
while True:
        if d.temperature() >= 21 and d.humidity() >= 70 and station.isconnected():
            r.value(1)
            print("Conectado!!!")
            print("Relé module activated")
            print("Its temperature is {}ºC and its humidity is {}%".format(d.temperature(), d.humidity()))
            station.connect()
            conectData()
            time.sleep(5)
        elif d.temperature() <= 21 and d.humidity() <= 70 and station.isconnected():
            r.value(0)
            print("Conectado!!!")
            print("Relé module disabled, its temperature is {}ºC > 31ºC and humidity is {}% > 70%".format(d.temperature(), d.humidity()))
            station.connect()
            conectData()
            time.sleep(5)
        else:
            print("Não conectado!")
            time.sleep(5)