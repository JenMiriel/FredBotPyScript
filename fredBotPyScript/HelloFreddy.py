#!/usr/bin/env python3
import pyautogui
import path

# if __name__ == '__main__':

print("Hello Freddy!")
print(pyautogui.size())
width, height = pyautogui.size()
print(pyautogui.position())
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveTo(200, 1000, duration=1.5)
pyautogui.moveTo(500, 500, duration=1)
pyautogui.moveTo(height - 100, width / 2, duration=1)
print(pyautogui.position())
