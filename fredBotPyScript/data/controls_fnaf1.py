# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room
from fredBotPyScript.data.image_manip import take_screenshot
from fredBotPyScript.data.image_manip import find_text_in_image
from fredBotPyScript.data.data_models import CInfo
import fredBotPyScript.data.data_models as Data_Models
import subprocess
import time
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'


# Left Side Controls
def check_left_door():
    print("check left door")
    print("camera up? ", CInfo.cameraUp)
    if CInfo.cameraUp:
        check_cameras(CInfo.cameraUp)
    x = 200
    y = CInfo.height / 3
    pyautogui.moveTo(x, y, duration=1)
    time.sleep(2)


def switch_left_hall_light():
    print("flip left hall light")
    print("camera up? ", CInfo.cameraUp)
    x = 200
    y = CInfo.height / 2
    print("move", x, y)
    pyautogui.moveTo(x, y, duration=1)
    print("click")
    pyautogui.click(55, 453)
    print("is left light on? ", CInfo.leftHallLightOn)
    CInfo.leftHallLightOn = not CInfo.leftHallLightOn
    print("is left light on? ", CInfo.leftHallLightOn)


def left_door():
    print("open/shut left door")
    print("camera up? ", CInfo.cameraUp)
    x = 200
    y = CInfo.height / 2
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click(55, 333)
    CInfo.leftDoorClosed = not CInfo.leftDoorClosed


# Right Side Controls
def check_right_door():
    print("check Right door")
    print("camera up? ", CInfo.cameraUp)
    if CInfo.cameraUp:
        check_cameras(CInfo.cameraUp)
    x = CInfo.width - 200
    y = CInfo.height / 3
    pyautogui.moveTo(x, y, duration=2)
    time.sleep(2)


def switch_right_hall_light():
    print("flip Right hall light")
    print("camera up? ", CInfo.cameraUp)
    x = CInfo.width - 200
    y = CInfo.height / 2
    pyautogui.moveTo(x, y, duration=1)
    x = CInfo.width - 55
    pyautogui.click(x, 453)
    CInfo.rightHallLightOn = not CInfo.rightHallLightOn


def right_door():
    print("open/shut Right door")
    print("camera up? ", CInfo.cameraUp)
    x = CInfo.width - 200
    y = CInfo.height / 2
    pyautogui.moveTo(x, y, duration=1)
    x = CInfo.width - 55
    pyautogui.click(x, 333)
    CInfo.rightDoorClosed = not CInfo.rightDoorClosed


# Security Camera Controls
def check_cameras(camera):
    print("toggle camera")
    x = CInfo.width / 2
    y = CInfo.height - 50
    pyautogui.moveTo(x, y, duration=1)
    camera = not camera  # toggle
    if camera:
        print("camera up")
    else:
        print("camera down")
    return camera


def camera_check_room(room_number):
    if not CInfo.cameraUp:
        CInfo.cameraUp = check_cameras(CInfo.cameraUp)
    x = CInfo.rooms[room_number].x_coord
    y = CInfo.rooms[room_number].y_coord
    pyautogui.moveTo(x, y, duration=1)
    print("Checking...", CInfo.rooms[room_number].long_name)
    room_empty = control_check_room(room_number)


# Misc functions
def start_game():
    # start game
    os.startfile(
       r"C:\Users\jenmi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Five Nights at Freddy's.url")

    # wait for boot
    time.sleep(9)

    # look at start options
    take_screenshot("main_menu")
    im = pyautogui.screenshot(region=(160, 400, 300, 200))
    im.save('resources\\screens\\temp.jpg')
    main_menu_options = find_text_in_image('resources\\screens\\temp.jpg')
    continue_or_nah = main_menu_options.find('Continue')

    if continue_or_nah < 0:
        # click new game
        print("New Game click")
        pyautogui.moveTo(222, 424, duration=1)
        pyautogui.leftClick()
    else:
        # click continue
        print("Continue Game click")
        pyautogui.moveTo(222, 494, duration=1)
        pyautogui.leftClick()

    # get and set screen size
    print(pyautogui.size())
    CInfo.width, CInfo.height = pyautogui.size()
    CInfo.rooms = Data_Models.initialize_room_locations(CInfo.width, CInfo.height)

    if continue_or_nah < 0:
        # wait for new game load
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(18)
    else:
        # wait for continue game load
        time.sleep(10)


def initialize_camera_screenshots():
    if CInfo.cameraUp:
        CInfo.cameraUp = check_cameras(CInfo.cameraUp)

    check_left_door()
    print("screenshotting Left Office")
    take_screenshot("left_office")

    switch_left_hall_light()
    print("screenshotting Left Office Light")
    take_screenshot("left_office_light")
    time.sleep(2)
    switch_left_hall_light()

    left_door()
    print("screenshotting Left Office Door")
    time.sleep(2)
    take_screenshot("left_office_door")

    switch_left_hall_light()
    print("screenshotting Left Office Door Light")
    time.sleep(2)
    take_screenshot("left_office_door_light")
    left_door()
    switch_left_hall_light()

    check_right_door()
    print("screenshotting Right Office")
    take_screenshot("right_office")

    switch_right_hall_light()
    print("screenshotting Right Office Light")
    time.sleep(2)
    take_screenshot("right_office_light")
    switch_right_hall_light()

    right_door()
    print("screenshotting Right Office Door")
    time.sleep(2)
    take_screenshot("right_office_door")

    switch_right_hall_light()
    print("screenshotting Right Office Door Light")
    time.sleep(2)
    take_screenshot("right_office_door_light")
    right_door()
    switch_right_hall_light()

    if not CInfo.cameraUp:
        CInfo.cameraUp = check_cameras(CInfo.cameraUp)
    take_screenshot()
    # take screens of all rooms
    for i in CInfo.rooms:
        print("screenshotting", CInfo.rooms[i].long_name, "at", CInfo.rooms[i].x_coord, "x", CInfo.rooms[i].y_coord)
        pyautogui.click(CInfo.rooms[i].x_coord, CInfo.rooms[i].y_coord)
        time.sleep(1)
        take_screenshot(CInfo.rooms[i].name)
    print("screenshots complete")


# Dummy functions
def control_check_room(room_number):
    is_clear = check_room(room_number)
    return is_clear
