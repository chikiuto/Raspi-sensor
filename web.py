import requests
from datetime import datetime

def uploadSensorValues(tmp, hum, press, name):
    # url にセンターのパソコンのIPアドレスを入れる
    url = 'http://127.0.0.1:8080/sensvalues.php'
    headers = { 'content-type': 'application/json' }
    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                   'temp':tmp,
                   'hum':hum,
                   'press':press,
                   'name':name}
    res = requests.post( url, headers=headers, json=sensorsdata, verify=False )
    print ( sensorsdata )
    print ( res.text )
    pass

def main():
    uploadSensorValues( 26.8, 58.9, 1012, 'nyaaaaaaaaa' )
 
if __name__ == '__main__':
    main()