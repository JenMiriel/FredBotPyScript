#!/usr/bin/env python3
import fredBotPyScript.data.controls_fnaf1


def run():
    print("Hello Freddy!")
    camera_up = fredBotPyScript.data.controls_fnaf1.cameraUp
    print("camera up: ", camera_up)

    fredBotPyScript.data.controls_fnaf1.check_left_door()
    fredBotPyScript.data.controls_fnaf1.check_right_door()

    camera_up = fredBotPyScript.data.controls_fnaf1.check_cameras(camera_up)
    print("camera up: ", camera_up)

    main_stage_clear = fredBotPyScript.data.controls_fnaf1.camera_main_stage()

    camera_up = fredBotPyScript.data.controls_fnaf1.check_cameras(camera_up)
    print("camera up: ", camera_up)

