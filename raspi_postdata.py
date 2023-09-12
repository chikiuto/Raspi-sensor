import smbus
import time
import requests
from datetime import datetime


# I2C設定
i2c = smbus.SMBus( 1 ) # インスタンス作成。使用する Bus1 を設定
address = 0x38 # DHT20 のアドレス指定

#トリガ設定コマンド
set = [0xAC, 0x33, 0x00] # センサーはこの 3byte を受け取ると測定を開始する

#データ読み込み用
dat = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] # センサーからは 7byte のデータが帰ってくる
# ステータス 8bit, 湿度データ 20bit, 温度データ 20bit, CRC 8bit ... 合計 56bit = 7byte
# ステータス：0x71 を送ると、0x81 が帰ってくる。
# 湿度データ：dat[1] + dat[2] + dat[3]の上位4bit = 合計20bit
# 温度データ：dat[3]の下位4bit + dat[4] + dat[5] = 合計20bit
# CRC (= 巡回冗長検査)：データ送信中にノイズなどで値が変化してしまった時に、間違いを発見するために使われる


# DHT20/AHT25設定
time.sleep(0.1)
ret = i2c.read_byte_data( address, 0x71 ) # ステータス確認

if ret != 0x18: # 0x81 が帰ってこなかったら処理終了
    exit 

# 繰り返し
# while 1:

# トリガ測定コマンド送信
time.sleep( 0.01 )
i2c.write_i2c_block_data( address, 0x00, set )

# データの読み込み、datに代入する
time.sleep( 0.08 )
dat = i2c.read_i2c_block_data( address, 0x00, 0x07 )

# データ変換
hum = dat[1] << 12 | dat[2] << 4 | ((dat[3] & 0xF0) >> 4)
tmp = ((dat[3] & 0x0F) << 16) | dat[4] << 8 | dat[5]

# 物理量変換
hum = hum / 2**20 * 100
tmp = tmp / 2**20 * 200 - 50

# 表示
print( "hum: " + str( hum ) )
print( "tmp: " + str( tmp ) )

time.sleep( 1 )


def uploadSensorValues( tmp, hum, press, name ):
    # url に送信先のパソコンのIPアドレスを入れる
    url = 'http://127.000.00.00:8080/sensvalues.php'
    headers = { 'content-type': 'application/json' }
    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                   'temp':tmp,
                   'hum':hum,
                   'press':press,
                   'name':name }
    res = requests.post( url, headers=headers, json=sensorsdata, verify=False )
    print ( sensorsdata )
    print ( res.text )
    pass

def main():
    uploadSensorValues( tmp, hum, 5555, 'nyaaaaaaaaa' )
 
if __name__ == '__main__':
    main()