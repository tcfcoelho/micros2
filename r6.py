import json
from requests import get
from pprint import pprint
import time
from picamera import PiCamera

oracleURL = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583"

weather = get(oracleURL).json()['items'][0]
pprint(weather)

camText = f"NUSP: 11372782 \nTemperatura: {weather['ambient_temp']}\n"
print(camText)

camera = PiCamera()
camera.resolution = (1024,768)

camera.start_preview()
time.sleep(2)
camera.annotate_text = camText
camera.capture('weatherpic.jpg')

# time.sleep(2)
# camera.start_recording('rec.h264')
# camera.wait_recording(5)
# camera.stop_recording()
# camera.stop_preview()