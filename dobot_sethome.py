from DobotDriver import DobotDriver 

dobot_arm = DobotDriver()

dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)
dobot_arm.set_home()
dobot_arm.move_on_robot_coordinate(0.205,0.0,0.15,0.0,wait=True)