# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room
import subprocess
import time
import os


class Room:
    def __init__(self, cam=0, name=0, long_name=0, stage=0):
        self.cam = cam
        self.name = name
        self.long_name = long_name
        self.stage = stage
        self.occupied = 0


class CInfo:
    # width = 720
    # height = 1280
    width = 640
    height = 480
    cameraUp = False
    leftHallLightOn = False
    rightHallLightOn = False
    leftDoorClosed = False
    rightDoorClosed = False
    time = 0
    power = 100
    night = 1


rooms = {"cam1a": Room("1A", "main", "Show Stage", 0),
         "cam1b": Room("1B", "dining", "Dining Area", 0),
         "cam1c": Room("1C", "pirate", "Pirate Cove", 0),
         "cam2a": Room("2A", "whall", "West Hall", 0),
         "cam2b": Room("2B", "whallc", "West Hall Corner", 0),
         "cam3": Room("3", "supply", "Supply Closet", 0),
         "cam4a": Room("4A", "ehall", "East Hall", 0),
         "cam4b": Room("4B", "ehallc", "East Hall Corner", 0),
         "cam5": Room("5", "backstage", "Backstage", 0),
         "cam6": Room("6", "kitchen", "Kitchen", 0),
         "cam7": Room("7", "restroom", "Restrooms", 0)}


# Left Side Controls
def check_left_door():
    pyautogui.moveTo(200, CInfo.height / 3, duration=1)
    time.sleep(2)


def switch_left_hall_light():
    pyautogui.moveTo(CInfo.width / 2, CInfo.height - 20, duration=1)


def left_door():
    pyautogui.moveTo(CInfo.width / 2, CInfo.height - 20, duration=1)


# Right Side Controls
def check_right_door():
    pyautogui.moveTo(CInfo.width - 200, CInfo.height / 3, duration=2)
    time.sleep(2)


def switch_right_hall_light():
    pyautogui.moveTo(CInfo.width / 2, CInfo.height - 20, duration=1)


def right_door():
    pyautogui.moveTo(CInfo.width / 2, CInfo.height - 20, duration=1)


# Security Camera Controls
def check_cameras(camera):
    pyautogui.moveTo(CInfo.width / 2, CInfo.height - 50, duration=1)
    camera = not camera  # toggle
    return camera


def camera_main_stage():
    pyautogui.moveTo(986, 355, duration=1)  # 986, 355
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

    # get screen size
    print(pyautogui.size())
    CInfo.width, CInfo.height = pyautogui.size()

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


