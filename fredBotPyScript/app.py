#!/usr/bin/env python3
import fredBotPyScript.data.controls_fnaf1 as control


def run():
    print("Hello Freddy!")
    control.start_game()
    # initialize screenshots
    control.initialize_camera_screenshots()

    control.CInfo.cameraUp = control.check_cameras(control.CInfo.cameraUp)

    control.check_left_door()
    control.check_right_door()

    # # check the dining room
    # control.camera_check_room("cam1b")
    #
    # # main_stage_clear = control.camera_main_stage()
    # # print("Is Main Stage Safe? ", main_stage_clear)
    #
    # control.CInfo.cameraUp = control.check_cameras(control.CInfo.cameraUp)
    #
