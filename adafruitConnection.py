from backend import setup
import requests
import json
import pickle
import pandas as pd
import datetime
import pytz
import time
from notification import send_push_message
setup()


from rain_forecast.models import User, Device
ADAFRUIT_IO_KEY = 'aio_wsVz16Oeun8i1wwDGe78fY6bhZEl'

userList = User.objects.all()
# At the moment, only the lastest user may have this service
devicesInfo = Device.objects.filter(user=userList[len(userList)-1]).exclude(type='Magnetic switch')
switchInfo = Device.objects.filter(user=userList[len(userList)-1], type='Magnetic switch')


push_token = ['ExponentPushToken[uPVhNdBgorULEX__74YHS2]']
def close_door_window(switchesInfo):
    for i in range(len(switchInfo)):
        response = requests.post('https://io.adafruit.com/api/v2/' + switchInfo[i].topic_name + '/data',
                                headers={
                                    "X-AIO-Key": ADAFRUIT_IO_KEY
                                },
                                data={
                                    "value":json.dumps(
                                        {
                                            "id": "8",
                                            "name": "MAGNETIC",
                                            "data": 1,
                                            "unit": "",
                                        }
                                    )
                                }
                                )


while 1:
    latest_humid = latest_temp = latest_rain = 0
    switches_stage = []
    for i in range(len(devicesInfo)):
        response = requests.get('https://io.adafruit.com/api/v2/' + devicesInfo[i].topic_name + '/data/last',
                                headers={"X-AIO-Key": ADAFRUIT_IO_KEY})
        info = json.loads(response.json()['value'])
        if info['name'] == 'RAIN':
            latest_rain = float(info['data'])
        elif info['name'] == 'TEMP-HUMID':
            latest_temp = float(info['data'].split('-')[0])
            latest_humid = float(info['data'].split('-')[1])

    for i in range(len(switchInfo)):
        response = requests.get('https://io.adafruit.com/api/v2/' + switchInfo[i].topic_name + '/data/last',
                                headers={"X-AIO-Key": ADAFRUIT_IO_KEY})
        info = json.loads(response.json()['value'])
        switches_stage.append(int(info['data']))

    model_file = 'model.sav'
    loaded_model = pickle.load(open(model_file, 'rb'))
    inputData = {'TempAvgF': latest_temp, 'HumidityAvgPercent': latest_humid, 'SeaLevelPressureAvgInches': latest_rain}
    inputDf = pd.DataFrame(inputData, index=[0])

    rainPercentage = loaded_model.predict(inputDf)[0]
    notification_title = notification_content = ""

    if rainPercentage > 0.8:
        if 1 in switches_stage:
            notification_title = "Warning!"
            notification_content = "It is going to rain soon\nClosed all the doors and windows."
            close_door_window(switchInfo)
            for x in push_token:
                send_push_message(x, notification_title, notification_content)

    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.datetime.now(tz)

    if now.hour == 6:
        notification_title = "Good morning!"
        notification_content = "Current temparature is : " + str(latest_temp) + "\nCurrent humidity is: " + str(latest_humid) + \
                               "\nChange of raining is " + rainPercentage + "%"
        for x in push_token:
            send_push_message(x, notification_title, notification_content)

    time.sleep(40)


