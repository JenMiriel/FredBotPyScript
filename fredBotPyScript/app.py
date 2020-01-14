#!/usr/bin/env python3
import fredBotPyScript.data.controls_fnaf1 as control


def run():
    print("Hello Freddy!")
    camera_up = control.CInfo.cameraUp
    rooms = control.rooms
    info = control.CInfo
    print("camera up: ", camera_up)

    control.start_game()

    control.check_left_door()
    control.check_right_door()

    control.CInfo.cameraUp = control.check_cameras(control.CInfo.cameraUp)
    print("camera up: ", control.CInfo.cameraUp)

    control.camera_check_room("cam1a")

    main_stage_clear = control.camera_main_stage()
    print("Is Main Stage Safe? ", main_stage_clear)

    control.CInfo.cameraUp = control.check_cameras(control.CInfo.cameraUp)
    print("camera up: ", control.CInfo.cameraUp)

