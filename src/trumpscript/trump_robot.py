import wpilib
import multiprocessing
import os
from src.trumpscript.compiler import *
from src.trumpscript.utils import *

trumpbot = None
compiled = {}


class TrumpRobot(wpilib.TimedRobot):
    def __init__(self):
        super(TrumpRobot, self).__init__()
        self.code = None
        global trumpbot
        trumpbot = self

    def robotInit(self):
        print("init")
        self.code = multiprocessing.Process(target=start_from_robot, args=["trumpcode/init.tr", True, False, True, set_compiled])
        self.code.start()

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        print("teleop")
        self.start_code("trumpcode/teleop.tr")

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        print("auton")
        self.start_code("trumpcode/auton.tr")

    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        self.start_code("trumpcode/disabled.tr")

    def disabledPeriodic(self):
        pass

    def start_code(self, file):
        self.code.terminate()
        self.code = multiprocessing.Process(target=start_from_robot, args=[file, True, False, True, set_compiled])
        self.code.start()


def set_compiled(value):
    print(value)
    global compiled
    compiled = value


def do_the_thing0(args):
    print("thing0")
    return 1


def do_the_thing1(args, args1):
    print("thing1")
    return 0


def start_from_robot(program, shut_up, wall, brainwash, compiled):
    if not os.path.isfile(program):
        print("Invalid file specified,")
        return

    # Decide whether to ignore system warnings
    if not shut_up:
        Utils.verify_system(wall)
    flip_flopping = not brainwash
    # Compile and go
    Compiler().compile(program, flip_flopping, compiled)

        
if __name__ == '__main__':
    wpilib.run(TrumpRobot, physics_enabled=True)