from machine import Pin, I2C
i2c = I2C(scl=Pin(12), sda=Pin(14))

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

from time import sleep

import wifimgr

import urequests

import ujson

#oled.text("SSD1306 Test",0,0)         #在指定坐标显示内容
#oled.text("12345678ABCDEFGH",0,16)
#oled.text("abcdefgh,.?!@#$%",0,26)

# 功能演示：
#oled.pixel(127,0,1)              #画点：  X坐标，y坐标
#oled.hline(0,40,15,1)            #画横线： X坐标，y坐标，宽度多少像素，颜色1
#oled.vline(20,40,15,1)           #画竖线： X坐标，y坐标，高度多少像素，颜色1
#oled.line(32,40, 48,55, 1)       #画两点之间的线：起点Xy坐标，终点xy坐标，颜色1
#oled.rect(60,40, 20,15, 1)       #画矩形： X坐标，y坐标，宽度，调试，颜色1
#oled.fill_rect(84,40, 20,15, 1)  #画矩形并填充：  X坐标，y坐标，宽度，调试，颜色1
#lcd.scroll(10,10)              #图像复制移位： 右移几个像素、下移几个像素

#正式显示
#oled.show()

oled_width = 128
oled_height = 64

wlan = wifimgr.get_connection()

url='https://devapi.qweather.com/v7/weather/now?key=d366904983894052b28be0974d8c022e&location=101180406'

key='d366904983894052b28be0974d8c022e'
location='101180406'

def get_live_weather_data():
#    payload = {'key': key, 'location': location}
    r=urequests.get('http://jsonplaceholder.typicode.com/users/1')
    print(r.text)
    parsed = ujson.loads(r.text)
    return parsed


uj = get_live_weather_data()

screen1_row1 = str(uj['name'])
screen1_row2 = str(uj['email'])
screen1_row3 = str(uj['phone'])

screen2_row1 = "Screen 2, row 1"
screen2_row2 = "Screen 2, row 2"

screen3_row1 = "Screen 3, row 1"

screen1 = [[0, 0 , screen1_row1], [0, 16, screen1_row2], [0, 32, screen1_row3]]
screen2 = [[0, 0 , screen2_row1], [0, 16, screen2_row2]]
screen3 = [[0, 40 , screen3_row1]]


# Scroll in screen horizontally from left to right
def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll out screen horizontally from left to right    
def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()

# Continuous horizontal scroll
def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)
 
# Scroll in screen vertically 
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)
      
# Scroll out screen vertically 
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()

# Continous vertical scroll
def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)


# Scroll in, stop, scroll out (horizontal)
scroll_in_screen(screen1)
sleep(1)
scroll_out_screen(4)

scroll_in_screen(screen2)
sleep(1)
scroll_out_screen(4)

scroll_in_screen(screen3)
sleep(1)
scroll_out_screen(4)

# Continuous horizontal scroll
scroll_screen_in_out(screen1)
scroll_screen_in_out(screen2)
scroll_screen_in_out(screen3)

# Scroll in, stop, scroll out (vertical)
scroll_in_screen_v(screen1)
sleep(1)
scroll_out_screen_v(4)

scroll_in_screen_v(screen2)
sleep(1)
scroll_out_screen_v(4)

scroll_in_screen_v(screen3)
sleep(1)
scroll_out_screen_v(4)

# Continuous verticall scroll 
scroll_screen_in_out_v(screen1)
scroll_screen_in_out_v(screen2)
scroll_screen_in_out_v(screen3)



