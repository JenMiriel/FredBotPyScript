import pyautogui


def check_room():
    # take screenshot
    take_screenshot()
    # see if screenshot has robot / image manip
    # if no robot, is_clear = True; if robot, is_clear = False
    is_room_empty = compare_images()
    return is_room_empty


def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(r'C:\Users\jenmi\OneDrive\Desktop\fredbotdata\compare.png')


def compare_images():
    # compare the images to the standard empty room
    are_images_similar = True
    return are_images_similar
