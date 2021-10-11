import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

while  True:
    d.measure()
    if d.temperature() >= 21 and d.humidity() >= 70:
        r.value(1)
        print("Relé module activated")
        print("Its temperature is {}ºC and its humidity is {}%".format(d.temperature(), d.humidity()))
        time.sleep(5)
    else:
        r.value(0)
        print("Relé module disabled, its temperature is {}ºC > 31ºC and humidity is {}% > 70%".format(d.temperature(), d.humidity()))
        time.sleep(5)