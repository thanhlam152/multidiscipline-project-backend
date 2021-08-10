import serial
import time
import requests
import json

ADAFRUIT_IO_KEY = "aio_uMEz97pgL6w0hdht4lj0mDEzq3Ca"

arduino = serial.Serial('/dev/cu.usbserial-14140', 9600, timeout=.1)
time.sleep(1)  # give the connection a second to settle

while True:
    data = arduino.readline()
    if data:
        received = data.decode('UTF-8')
        if 'Analog value' in received:
            value = int(received.split()[2])
            print(value)
            if value > 500:
                value = 0

            response = requests.post('https://io.adafruit.com/api/v2/LeThanh/feeds/rain-sensor/data',
                                     headers={
                                         "X-AIO-Key": ADAFRUIT_IO_KEY
                                     },
                                     data={
                                         "value": json.dumps(
                                             {
                                                 "id": "25",
                                                 "name": "RAIN",
                                                 "data": str(value),
                                                 "unit": "mm",
                                             }
                                         )
                                     }
                                     )
