# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room
from fredBotPyScript.data.image_manip import take_screenshot
from fredBotPyScript.data.image_manip import find_text_in_image
import subprocess
import time
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'


class Room:
    def __init__(self, cam="de", name="default", long_name="default", stage=0, occupied=0, screen_width=640, screen_height=480, x_coord=0, y_coord=0):
        self.cam = cam
        self.name = name
        self.long_name = long_name
        self.stage = stage
        self.occupied = 0
        self.x_coord = round(screen_width * x_coord)
        self.y_coord = round(screen_height * y_coord)


class CInfo:
    # height = 720
    # width = 1280
    height = 480
    width = 640
    cameraUp = False
    leftHallLightOn = False
    rightHallLightOn = False
    leftDoorClosed = False
    rightDoorClosed = False
    time = 0
    power = 100
    night = 1
    rooms = {"default": Room()}


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
    CInfo.rooms = initialize_room_locations(CInfo.width, CInfo.height)

    if continue_or_nah < 0:
        # wait for new game load
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(18)
    else:
        # wait for continue game load
        time.sleep(10)

    # click continue game
    # pyautogui.moveTo(width - 100, height / 2, duration=1)
    # pyautogui.leftClick()


def initialize_room_locations(screen_width, screen_height):
    # 1280 x 720
    print("should be 986 x 355:", round(screen_width * .77), "x", round(screen_height * .49))
    init_rooms = {"cam1a": Room("1A", "main", "Show Stage", 0, 1, screen_width, screen_height, .77, .49),  # 986, 355
                  "cam1b": Room("1B", "dining", "Dining Area", 0, 0, screen_width, screen_height, .75, .56),  # 958, 406
                  "cam1c": Room("1C", "pirate", "Pirate Cove", 1, 1, screen_width, screen_height, .72, .67),  # 927, 485
                  "cam2a": Room("2A", "whall", "West Hall", 0, 0, screen_width, screen_height, .76, .82),  # 977, 589
                  "cam2b": Room("2B", "whallc", "West Hall Corner", 0, 0, screen_width, screen_height, .77, .89),  # 982, 641
                  "cam3": Room("3", "supply", "Supply Closet", 0, 0, screen_width, screen_height, .70, .81),  # 897, 585
                  "cam4a": Room("4A", "ehall", "East Hall", 0, 0, screen_width, screen_height, .85, .83),  # 1088, 601
                  "cam4b": Room("4B", "ehallc", "East Hall Corner", 0, 0, screen_width, screen_height, .85, .89),  # 1085, 640
                  "cam5": Room("5", "backstage", "Backstage", 0, 0, screen_width, screen_height, .67, .60),  # 858, 434
                  "cam6": Room("6", "kitchen", "Kitchen", 0, 0, screen_width, screen_height, .92, .79),  # 1183, 567
                  "cam7": Room("7", "restroom", "Restrooms", 0, 0, screen_width, screen_height, .93, .60)}  # 1192, 435
    return init_rooms


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
