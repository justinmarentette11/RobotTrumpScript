import wpilib
from src.trumpscript.main import *
import multiprocessing

trumpbot = None


class TrumpRobot(wpilib.TimedRobot):
    def __init__(self):
        super(TrumpRobot, self).__init__()
        self.code = None
        global trumpbot
        trumpbot = self

    def robotInit(self):
        print("init")
        self.code = multiprocessing.Process(target=start_from_robot, args=["trumpcode/init.tr", True, False, True])
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
        self.code = multiprocessing.Process(target=start_from_robot, args=[file, True, False, True])
        self.code.start()


def do_the_thing0(args):
    print("thing0")
    return 1


def do_the_thing1(args, args1):
    print("thing1")
    return 0


if __name__ == '__main__':
    wpilib.run(TrumpRobot, physics_enabled=True)
