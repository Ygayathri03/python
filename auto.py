lfrom pynput.keyboard import Key,Controller
import time
import random
keyboard=Controller()
time.sleep(4)
content=''' This content will be printed by the keyboard
automatically without typing. pynput takes the control of keyboard and mouse 

'''
for i in range(5):
    for char in content:
        keyboard.type(char)
        time.sleep(random.uniform(0.1,0.5))
