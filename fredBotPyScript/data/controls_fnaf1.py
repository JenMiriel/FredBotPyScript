# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room

print(pyautogui.size())
width, height = pyautogui.size()
cameraUp = False
leftHallLightOn = False
rightHallLightOn = False
leftDoorClosed = False
rightDoorClosed = False


# Left Side Controls
def check_left_door():
    pyautogui.moveTo(20, height / 2, duration=1)


def switch_left_hall_light():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


def left_door():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


# Right Side Controls
def check_right_door():
    pyautogui.moveTo(width - 20, height / 2, duration=1)


def switch_right_hall_light():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


def right_door():
    pyautogui.moveTo(width / 2, height - 20, duration=1)


# Security Camera Controls
def check_cameras(camera):
    pyautogui.moveTo(width / 2, height - 20, duration=1)
    camera = not camera  # toggle
    return camera


def camera_main_stage():
    pyautogui.moveTo(width - 100, height / 2, duration=1)
    room_empty = control_check_room()
    if room_empty:
        print("main stage empty")
    return room_empty


# Dummy functions
def control_check_room():
    is_clear = check_room()
    return is_clear


