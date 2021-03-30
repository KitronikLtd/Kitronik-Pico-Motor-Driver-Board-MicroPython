import PicoMotorDriver
import utime

board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

Input1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
Input2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

Input3 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
Input4 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# Switch out Input 1 and 2 for Input 3 and 4 as part of testing

while True:
    if(Input1.value())
        direction1 = "f"
    else:
        direction1 = "r"
    if(Input2.value())
        direction2 = "f"
    else:
        direction2 = "r"
    board.motorOn(1, direction1, 75)
    board.motorOn(2, direction2, 75)

                