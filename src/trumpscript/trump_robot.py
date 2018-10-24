import wpilib
import multiprocessing
import os
from src.trumpscript.compiler import *
from src.trumpscript.utils import *

trumpbot = None
compiled = {}
objects = {}


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


def create_adxl345_i2c(port, range):
    return wpilib.ADXL345_I2C(port, range)


def create_adxl345_spi(port, range):
    return wpilib.ADXL345_SPI(port, range)


def create_adxl362(range, port=None):
    return wpilib.ADXL362(range, port)


def create_adxrs450_gyro(port=None):
    return wpilib.ADXRS450_Gyro(port)


def create_analog_accelerometer(channel):
    return wpilib.AnalogAccelerometer(channel)


def create_analog_gyro(channel):
    return wpilib.AnalogGyro(channel)


def create_analog_input(channel):
    return wpilib.AnalogInput(channel)


def read_analog(analog):
    return analog.getVoltage()


def read_average_analog(analog):
    return analog.getAverageVoltage()


def create_analog_output(channel):
    return wpilib.AnalogOutput(channel)


def create_analog_potentiometer(channel):
    return wpilib.AnalogPotentiometer(channel)
    

def create_analog_trigger(channel):
    return wpilib.AnalogTrigger(channel)
    

def create_analog_trigger_output(trigger, type):
    return wpilib.AnalogTriggerOutput(trigger, type)
    

def create_built_in_accelerometer(range=2):
    return wpilib.BuiltInAccelerometer(range)
    

def create_camera_server():
    return wpilib.CameraServer()
    

def create_compressor(module=none):
    return wpilib.Compressor(module)
    

def create_controller_power():
    return wpilib.ControllerPower()
    

def create_counter(*args):
    return wpilib.Counter(args)
    

def create_digital_glitch_filter():
    return wpilib.DigitalGlitchFilter()
    

def create_digital_input(channel):
    return wpilib.DigitalInput(channel)
    

def create_digital_output(channel):
    return wpilib.DigitalOutput(channel)
    

def create_digital_source():
    return wpilib.DigitalSource()
    

def create_dmc60(channel):
    return wpilib.DMC60(channel)
    

def create_double_solenoid(*args):
    return wpilib.DoubleSolenoid(args)
    

def create_driver_station():
    return wpilib.DriverStation()
    

def create_encoder(*args):
    return wpilib.Encoder(args)
    

def create_filter(source):
    return wpilib.Filter(source)
    

def create_gear_tooth(channel, directionSensitive=False):
    return wpilib.GearTooth(channel, directionSensitive)
    

def create_gyro_base():
    return wpilib.GyroBase()
    

def create_i2c(port, deviceAddress, simPort=None):
    return wpilib.I2C(port, deviceAddress, simPort)
    

def create_interruptable_sensor_base():
    return wpilib.InterruptableSensorBase()
    

def create_iterative_robot():
    return wpilib.IterativeRobot()
    

def create_iterative_robot_base():
    return wpilib.IterativeRobotBase()
    

def create_():
    return wpilib.()


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
