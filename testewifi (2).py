import dht
import machine
import time
from socket import *
import network
import time
import urequests


def connect(ssid,senha):
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid,senha)
    for i in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station


def ligarDesligarRele():
    r = machine.Pin(2, machine.Pin.OUT)
    d.measure()
        
    temp = d.temperature()
    humidity = d.humidity()
    
    if temp > 31 or humidity > 70:
        r.value(1)
        print("Rele ligado!")
    else:
        r.value(0)
        print("Rele Desligado!")


print("Conectando a rede wifi...")
station = connect("SEREIA_2.4","WPA5522.123")
time.sleep(3)
if not station.isconnected():
    print("Não foi possível conectar a rede!")
else:
    print("Sucesso na conexão!")
    time.sleep(1)
    
    
    d= dht.DHT11(machine.Pin(4))
    d.measure()
    temp = d.temperature()
    humidity = d.humidity()
    time.sleep(1)
    
    print()
    print("Obtendo temperatura e humidade...")
    time.sleep(3)
    print("Temperatura atual:",temp,"°C")
    time.sleep(2)
    print("Humidade atual:",humidity,"%")
    time.sleep(3)
    print()
    print("Status do Rele: ")
    time.sleep(3)
    ligarDesligarRele()
    time.sleep(3)
    
    print("\nAcessando o ThingSpeak...")
    time.sleep(3)
    print("Enviando os dados... ")
    time.sleep(3)
    resposta = urequests.get("https://api.thingspeak.com/update?api_key=BSW9HVMT2XWZS1QW&field1={}&field2={}".format(temp,humidity))
   
           
    print("Dados enviados com Sucesso...!")
    
    
    print(resposta.text)
    resposta.close()
    station.disconnect()
    time.sleep(15)
       
