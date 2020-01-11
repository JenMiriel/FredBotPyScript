#!/usr/bin/env python3
import fredBotPyScript.data.controls_fnaf1 as control


def run():
    print("Hello Freddy!")
    camera_up = control.CInfo.cameraUp
    print("camera up: ", camera_up)

    control.start_game()

    control.check_left_door()
    control.check_right_door()

    camera_up = control.check_cameras(camera_up)
    print("camera up: ", camera_up)

    main_stage_clear = control.camera_main_stage()
    print("Is Main Stage Safe? ", main_stage_clear)

    camera_up = control.check_cameras(camera_up)
    print("camera up: ", camera_up)

