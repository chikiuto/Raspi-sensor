import requests
from datetime import datetime

def uploadSensorValues(temp, hum, press):

    url = 'http://127.0.0.1:8080/sensvalues.php'

    headers = {'content-type': 'application/json'}

    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'temp':temp,'hum':hum,'press':press}

    res = requests.post( url, headers=headers, json=sensorsdata, verify=False)

    print (sensorsdata)
    print (res.text)
    pass

def main():
    uploadSensorValues(11.9, 77.7, 5555)
 
if __name__ == '__main__':
    main()