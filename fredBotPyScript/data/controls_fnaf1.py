# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room
import subprocess
import time
import os

print(pyautogui.size())
width, height = pyautogui.size()
cameraUp = False
leftHallLightOn = False
rightHallLightOn = False
leftDoorClosed = False
rightDoorClosed = False


# Left Side Controls
def check_left_door():
    pyautogui.moveTo(200, height / 3, duration=1)
    time.sleep(2)


def switch_left_hall_light():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


def left_door():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


# Right Side Controls
def check_right_door():
    pyautogui.moveTo(width - 900, height / 3, duration=2)
    time.sleep(2)


def switch_right_hall_light():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


def right_door():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


# Security Camera Controls
def check_cameras(camera):
    pyautogui.moveTo(width / 2, height - 100, duration=1)
    camera = not camera  # toggle
    return camera


def camera_main_stage():
    pyautogui.moveTo(width - 100, height / 2, duration=1)
    room_empty = control_check_room()
    if room_empty:
        print("main stage empty")
    return room_empty


# Misc functions
def start_game():
    # start game
    os.startfile(r"C:\Users\jenmi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Five Nights at Freddy's.url")

    # wait for boot
    time.sleep(8)

    # click new game
    pyautogui.moveTo(222, 424, duration=1)
    pyautogui.leftClick()
    # wait for new game load
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(18)

    # click continue game
    # pyautogui.moveTo(width - 100, height / 2, duration=1)
    # pyautogui.leftClick()

# Dummy functions
def control_check_room():
    is_clear = check_room()
    return is_clear


