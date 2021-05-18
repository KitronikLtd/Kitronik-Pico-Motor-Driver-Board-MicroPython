# Kitronik-Pico-Motor-Driver-Board-MicroPython
A class and sample code to use the Kitronik Motor driver board for Raspberry Pi Pico. (www.kitronik.co.uk/5331)
To use save PicoMotorDriver.py file onto the Pico so it can be imported
## Import PicoMotorDriver.py and construct an instance:
    import PicoMotorDriver
    board = PicoMotorDriver.KitronikPicoMotor()

This will setup the correct pins to drive the motors. 
## Drive a motor:
    board.motorOn(motor, direction, speed)
where:
* motor => 1 or 2
* direction => f or r
* speed => 0 to 100
## Stop a motor:
    board.motorOff(motor)
where:
* motor => 1 or 2

## Drive a Stepper:
    board.step(direction,steps)
where:
* direction => f or r
* steps => how many steps to make

### To step an angle:
    stepAngle(direction, angle)
where
* direction => f or r
* steps => how many steps to make

The stepper code assumes 200 steps per rev (1.8 degrees resolution) and only does full steps. 
There are defaulted parameters for 
* stepper speeds (default 20mS pause between steps), 
* hold position when finished stepping (off - saves energy) 
* how many steps per rev (200).
Look at the function headers and function comments for more detail if you need to change them.

# Troubleshooting

This code is designed to be used as a module. See: https://kitronik.co.uk/blogs/resources/modules-micro-python-and-the-raspberry-pi-pico for more information

