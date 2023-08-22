import smbus
import time
import requests
from datetime import datetime


# I2C設定
i2c = smbus.SMBus(1)
address = 0x38

#トリガ設定コマンド
set = [0xAC, 0x33, 0x00]

#データ読み込み用
dat = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# DHT20/AHT25設定
time.sleep(0.1)
ret = i2c.read_byte_data(address, 0x71)

# if ret != 0x18:
    # initialization process

# 繰り返し
# while 1:

# トリガ測定コマンド送信
time.sleep(0.01)
i2c.write_i2c_block_data(address, 0x00, set)

# データの読み込み
time.sleep(0.08)
dat = i2c.read_i2c_block_data(address, 0x00, 0x07)

# データ変換
hum = dat[1] << 12 | dat[2] << 4 | ((dat[3] & 0xF0) >> 4)
tmp = ((dat[3] & 0x0F) << 16) | dat[4] << 8 | dat[5]

# 物理量変換
hum = hum / 2**20 * 100
tmp = tmp / 2**20 * 200 - 50

# 表示
print("hum: " + str(hum))
print("tmp: " + str(tmp))

time.sleep(1)


def uploadSensorValues(tmp, hum, press):

    url = 'http://127.000.00.00:8080/sensvalues.php'
    headers = { 'content-type': 'application/json' }
    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                   'temp':tmp,
                   'hum':hum,
                   'press':press}
    res = requests.post( url, headers=headers, json=sensorsdata, verify=False )
    print ( sensorsdata )
    print ( res.text )
    pass

def main():
    uploadSensorValues( tmp, hum, 5555 )
 
if __name__ == '__main__':
    main()