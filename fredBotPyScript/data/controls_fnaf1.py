# define controls for FNaF 1
import pyautogui
from fredBotPyScript.data.image_manip import check_room
from fredBotPyScript.data.image_manip import initialize_camera_screenshots
from fredBotPyScript.data.image_manip import take_screenshot
import subprocess
import time
import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'


class Room:
    def __init__(self, cam=0, name=0, long_name=0, stage=0, occupied=0, x_coord=0, y_coord=0):
        self.cam = cam
        self.name = name
        self.long_name = long_name
        self.stage = stage
        self.occupied = 0
        self.x_coord = 0
        self.y_coord = 0


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


rooms = {}


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
    print("Checking...", rooms["cam1a"].long_name)
    room_empty = control_check_room("cam1a")
    if room_empty:
        print("main stage empty")
    return room_empty


def camera_check_room(room_number):
    pyautogui.moveTo(986, 355, duration=1)
    print("Checking...", rooms[room_number].long_name)
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
    im = pyautogui.screenshot(region=(160, 400, 385, 515))
    # im.save('resources\\temp.jpg')
    # im = Image.open("resources\\temp.jpg")  # the second one
    # im = im.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(im)
    # im = enhancer.enhance(2)
    # im = im.convert('1')
    # im.save('resources\\temp2.jpg')
    # text = pytesseract.image_to_string(Image.open('resources\\temp2.jpg'))
    # print(text)

    # click new game
    pyautogui.moveTo(222, 424, duration=1)
    pyautogui.leftClick()

    # get screen size
    print(pyautogui.size())
    CInfo.width, CInfo.height = pyautogui.size()
    rooms = initialize_room_locations(CInfo.width, CInfo.height)

    # wait for new game load
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(18)

    # click continue game
    # pyautogui.moveTo(width - 100, height / 2, duration=1)
    # pyautogui.leftClick()

    # initialize screenshots
    initialize_camera_screenshots()


def initialize_screenshots():
    # go get dem
    time.sleep(2)


def initialize_room_locations(screen_width, screen_height):
    # 1280 x 720
    init_rooms = {"cam1a": Room("1A", "main", "Show Stage", 0, 1, 986, 355),  # 986, 355
                  "cam1b": Room("1B", "dining", "Dining Area", 0, 0, 958, 406),  # 958, 406
                  "cam1c": Room("1C", "pirate", "Pirate Cove", 1, 1, 927, 485),  # 927, 485
                  "cam2a": Room("2A", "whall", "West Hall", 0, 0, 977, 598),  # 977, 589
                  "cam2b": Room("2B", "whallc", "West Hall Corner", 0, 0, 982, 641),  # 982, 641
                  "cam3": Room("3", "supply", "Supply Closet", 0, 0, 897, 585),  # 897, 585
                  "cam4a": Room("4A", "ehall", "East Hall", 0, 0, 1088, 601),  # 1088, 601
                  "cam4b": Room("4B", "ehallc", "East Hall Corner", 0, 0, 1085, 640),  # 1085, 640
                  "cam5": Room("5", "backstage", "Backstage", 0, 0, 858, 434),  # 858, 434
                  "cam6": Room("6", "kitchen", "Kitchen", 0, 0, 1183, 567),  # 1183, 567
                  "cam7": Room("7", "restroom", "Restrooms", 0, 0, 1192, 435),  # 1192, 435
                  "office": Room("0", "office", "Office", 0, 0, 0, 0)}
    return init_rooms


# Dummy functions
def control_check_room(room_number):
    is_clear = check_room(room_number)
    return is_clear
