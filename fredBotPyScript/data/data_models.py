# define data models
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
