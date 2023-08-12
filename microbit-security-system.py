# Imports go at the top
from microbit import *
import time

# Code in a 'while True:' loop repeats forever
while True :
    if pin2.read_digital()==1:
        pin0.write_digital(1)
        sleep(2000)
        pin1.write_digital(1)
        
    if pin2.read_digital()==0:
        pin0.write_digital(0)
        pin1.write_digital(0)
