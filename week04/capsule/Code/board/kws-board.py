
from machine import Pin, ADC
from dht import DHT11
import utime, ujson, network, urequests, json

ANALOG_PIN = 0 #A0
BULDIN_LED_PIN = 2
DHT11_PIN = 13 #D7
LOCATION = "Borey V10" #Change here



def post_data(payload):
  """ Post the data to API server"""

  
  url = 'http://10.10.11.137:8019/posts/v0.1/weather' #Change here
  headers = {'content-type': 'application/json'} #Allow to pass JSON data with HTTPS protocol
  
  try:
    response = urequests.post(url, data = payload, headers = headers)
    parsed = response.json()
    if parsed['code'] == 200:
      print("Posted Successfully.")
    else:
      print("!!Posted Failed!!")
    response.close()
    
    return True
  except Exception as e:
    print("!!Posted Failed!! - ", e)
    return False
    
def ap_mode(mode):
  """" Turn off the AP mode on ESP8266"""
  
  wifiap = network.WLAN(network.AP_IF)
  wifiap.active(mode)
  if wifiap.active() == False:
    print("AP-Mode Diable Successfully :)")
  
def connect_wifi(ssid, password):
  """ Collecting to the network with pre-define ssid and password"""
  
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Network connected - IP:", station.ifconfig()[0])     
      return

  station.active(True)
  station.connect(ssid, password)

  while station.isconnected() == False:
      pass
 
  print("Connection successful")
  print(station.ifconfig())
  
def temp_humi_reader():
    """ Give the temperature in Celcius and Humidity in % """
    
    temp_humi_sensor = DHT11(Pin(DHT11_PIN))
    temp_humi_sensor.measure()
  
    return {
        "temp" : temp_humi_sensor.temperature(),
        "humi" : temp_humi_sensor.humidity()
    }

def water_reader():
    """ Give the status of rain (True or False) """
    
    digital_input = ADC(0)
    water_level = digital_input.read()
    status = 0

    if water_level <= 100:
      status = 0
    else:
      status = 1

    return { 
      "status" : status,
      "level" : water_level
    }

def led_working(status):
    """ LED feedback of the working status blink 0.5sec """
    
    led = Pin(BULDIN_LED_PIN, Pin.OUT)
    
    if status:
      led.value(1)#turn off
      utime.sleep(0.5)
      led.value(0)#turn on
      utime.sleep(0.5)
    else:
      for i in range(3):
        led.value(1)#turn off
        utime.sleep(0.1)
        led.value(0)#turn on
        utime.sleep(0.1)
  
def collect_data():
  """"Collecting temp, humi, and rain status and return as JSON"""
 
  data_package = dict()
  if temp_humi_reader() and water_reader():
    data_package["dht11"] = temp_humi_reader()
    data_package["rain"] = water_reader()
    data_package["location"] = LOCATION
    
    return ujson.dumps(data_package)
  else:
    print("!Error!")
    
    return False


#START HERE
if __name__ == "__main__":
  """ Program start from here"""
  
  #diable the ap mode on ESP
  ap_mode(False)
  
  #connect to the network
  ssid = "Borey R-J37" #Change here
  password = "" #Change here
  connect_wifi(ssid, password)
  running = True
  
  while running:
    data = collect_data()
    status = post_data(data)
    led_working(status)



