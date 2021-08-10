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

isPredictFirstTime = 0
userList = User.objects.all()
# At the moment, only the lastest user may have this service
devicesInfo = Device.objects.filter(user=userList[len(userList)-1]).exclude(type='Magnetic switch')
switchInfo = Device.objects.filter(user=userList[len(userList)-1], type='Magnetic switch')


push_token = ['ExponentPushToken[psuQ8ZGEELL-Twb17-6-SD]']
def close_door_window(switchesInfo):
    for i in range(len(switchInfo)):
        response = requests.post('https://io.adafruit.com/api/v2/' + switchInfo[i].topic_name + '/data',
                                headers={
                                    "X-AIO-Key": switchesInfo[i].aio_key
                                },
                                data={"value":"{\"id\":\"11\",\"name\":\"RELAY\",\"data\":\"1\",\"unit\":\"\"}"}
                                )
        print(response.json())


while 1:
    latest_humid = latest_temp = latest_rain = 0
    switches_stage = []
    for i in range(len(devicesInfo)):
        response = requests.get('https://io.adafruit.com/api/v2/' + devicesInfo[i].topic_name + '/data/last',
                                headers={"X-AIO-Key": devicesInfo[i].aio_key})
        info = json.loads(response.json()['value'])
        if info['name'] == 'RAIN':
            latest_rain = float(info['data'])
        elif info['name'] == 'TEMP-HUMID':
            latest_temp = float(info['data'].split('-')[0])
            latest_humid = float(info['data'].split('-')[1])

    for i in range(len(switchInfo)):
        response = requests.get('https://io.adafruit.com/api/v2/' + switchInfo[i].topic_name + '/data/last',
                                headers={"X-AIO-Key": switchInfo[i].aio_key})
        info = json.loads(response.json()['value'])
        switches_stage.append(int(info['data']))

    model_file = 'model.sav'
    loaded_model = pickle.load(open(model_file, 'rb'))

    if latest_rain < 10:
        rainPercentage = 0.1
    else:
        if (latest_humid<70):
            latest_humid = 70
        inputData = {'TempAvgF': latest_temp, 'HumidityAvgPercent': latest_humid, 'SeaLevelPressureAvgInches': 100}
        inputDf = pd.DataFrame(inputData, index=[0])

        rainPercentage = loaded_model.predict(inputDf)[0]
        notification_title = notification_content = ""
    print(rainPercentage)
    if rainPercentage > 0.5:
        if 0 in switches_stage:
            print(isPredictFirstTime)
            if  isPredictFirstTime <2:
                notification_title = "Warning!"
                notification_content = str(round(rainPercentage*100))+ "% it is going to rain soon!\nClosed all the doors and " \
                                                                "windows. "
                close_door_window(switchInfo)
                for x in push_token:
                    send_push_message(x, notification_title, notification_content)
                isPredictFirstTime +=1

    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.datetime.now(tz)

    if now.hour == 6:
        notification_title = "Good morning!"
        notification_content = "Current temparature is : " + str(latest_temp) + "\nCurrent humidity is: " + str(latest_humid) + \
                               "\nChange of raining is " + rainPercentage + "%"
        for x in push_token:
            send_push_message(x, notification_title, notification_content)

    time.sleep(1)


