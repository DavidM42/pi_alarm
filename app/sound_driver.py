from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import os
import time

from app import app

class SoundDriver(object):

    def __init__(self):
        print ""

    def on(self):
        print "Starting Sound:"
        os.system("sudo /home/pi/raspberry-remote/send 11111 1 1")


    def off(self):
        print "Turning sound things off"
        os.system("sudo /home/pi/raspberry-remote/send 11111 1 0")
