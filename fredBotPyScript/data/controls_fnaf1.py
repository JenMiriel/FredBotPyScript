#define controls for FNaF 1
import pyautogui

print(pyautogui.size())
width, height = pyautogui.size()

def CheckLeftDoor():
    pyautogui.moveTo(20, height / 2, duration=1)

def CheckRightDoor():
    pyautogui.moveTo(width - 20, height / 2, duration=1)
