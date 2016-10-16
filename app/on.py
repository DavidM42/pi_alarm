#!/usr/bin/env python
from light_driver import LightDriver
from sound_driver import SoundDriver
from multiprocessing import Process
import sys
import time
import os

def main():
    lightdriver = LightDriver()
    sounddriver = SoundDriver()
    soundProcess = Process(target = sounddriver.on)
    soundProcess.start()
    # lightProcess = Process(target = lightdriver.on)
    # lightProcess.start()


    lightdriver.init_on()
    no_interrupt = True
    i = 2
    while no_interrupt == True and i <= 27:
        lightdriver.repeat_on(i)
        i += 1
        print i
        if i == 7:
            no_interrupt = False

    sounddriver.off()
    lightdriver.laterMode()

if __name__ == "__main__":
	main()
