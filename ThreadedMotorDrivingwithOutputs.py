import PicoMotorDriver
import utime
import _thread

board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

Output1 = machine.Pin(0, machine.Pin.OUT)
Output2 = machine.Pin(1, machine.Pin.OUT)
Output3 = machine.Pin(26, machine.Pin.OUT)
Output4 = machine.Pin(27, machine.Pin.OUT)

Output1.value(0)
Output2.value(0)
Output3.value(0)
Output4.value(0)


def ThreadedDriveMotor():
    while True:
        for direction in directions:
            board.motorOn(1, direction, 80)
            board.motorOn(2, direction, 80)
            utime.sleep_ms(2000)
            board.motorOn(1, direction, 80)
            board.motorOn(2, direction, 80)
            utime.sleep_ms(2000)


_thread.start_new_thread(ThreadedDriveMotor,())

while True:
    Output1.value(1)
    utime.sleep_ms(500)
    Output1.value(0)
    Output2.value(1)
    utime.sleep_ms(500)
    Output2.value(0)
    Output3.value(1)
    utime.sleep_ms(500)
    Output3.value(0)
    Output4.value(1)
    utime.sleep_ms(500)
    Output4.value(0)