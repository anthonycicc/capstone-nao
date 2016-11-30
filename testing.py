import lib.beginner as beg

robot = beg.Beginner_Functions("localhost", 9559)

robot.say("Fuck you motherfucka")

robot.sit()
robot.reset_to_neutral()

robot.move_forward(5)
robot.reset_to_neutral()

robot.move_backward(5)
robot.reset_to_neutral()

robot.move_right(5)

robot.move_left(5)

robot.raise_right_arm(2)

robot.raise_left_arm(3)

# robot.kick("R")

robot.extend_arm('R')

