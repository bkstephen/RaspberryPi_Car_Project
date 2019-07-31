import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)


def forward():
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(11, True)
    gpio.output(7, False)
    time.sleep(1)

def backward():
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(11, False)
    gpio.output(7, True)
    time.sleep(1)

def right():
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(11, True)
    gpio.output(7, False)
    time.sleep(1)

def left():
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(11, False)
    gpio.output(7, True)
    time.sleep(1)

for i in range (0,10):
    left()

gpio.cleanup()
