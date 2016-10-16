from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import os
import time
import wifileds

from app import app

class LightDriver(object):

    def __init__(self, pin=None):
        print ""

    def init_on(self):
        print "Turning light on:"
        led_connection = wifileds.limitlessled.connect('192.168.178.101', 8899)
        led_connection.rgbw.set_brightness(2)
        led_connection.rgbw.set_color('orange')
        i = 2

    def repeat_on(self,i):
            led_connection = wifileds.limitlessled.connect('192.168.178.101', 8899)
            led_connection.rgbw.set_brightness(i)
            if i <= 16:
                if i == 17:
                    led_connection.rgbw.set_color('yellow_orange',1)
                time.sleep(8.6) # 2 minutes to this mode
            else:
                time.sleep(6) # other 11 steps in 1 min
            print "runnning "

    def laterMode(self):
        print "Making white and later off"
        led_connection = wifileds.limitlessled.connect('192.168.178.101', 8899)
        led_connection.rgbw.white(1)
        led_connection.rgbw.set_color('orange',2)
        led_connection.rgbw.set_brightness(19,2)
        led_connection.rgbw.set_brightness(23,1)

        time.sleep(40*60)
        led_connection.rgbw.all_off()
