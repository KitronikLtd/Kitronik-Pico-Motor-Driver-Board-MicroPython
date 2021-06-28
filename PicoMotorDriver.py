import machine
import utime

class KitronikPicoMotor:
    #Pins 4 and 5 motor 1
    #Pins 9 and 10 motor 2
    #'Forward' is P5 or P9 driven high, with P4 or P10 held low.
    #'Reverse' is P4 or P10 driven high, with P5 or P9 held low
   
    #Driving the motor is simpler than the servo - just convert 0-100% to 0-4095 and push it to the correct registers.
    #each motor has 4 writes - low and high bytes for a pair of registers. 
    def motorOn(self,motor, direction, speed):
        #cap speed to 0-100%
        if (speed<0):
            speed = 0
        elif (speed>100):
            speed=100
        #convert 0-100 to 0-65535
        PWM = int(speed*655.35)
        if motor == 1:
            if direction == "f":
                self.motor1Forward.duty_u16(PWM)
                self.motor1Reverse.duty_u16(0)
            elif direction == "r":
                self.motor1Forward.duty_u16(0)
                self.motor1Reverse.duty_u16(PWM)
            else:
                raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
        elif motor == 2:
            if direction == "f":
                self.motor2Forward.duty_u16(PWM)
                self.motor2Reverse.duty_u16(0)
            elif direction == "r":
                self.motor2Forward.duty_u16(0)
                self.motor2Reverse.duty_u16(PWM)
            else:
                raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
        else:
            raise Exception("INVALID MOTOR") #harsh, but at least you'll know
    #To turn off set the speed to 0...
    def motorOff(self,motor):
        self.motorOn(motor,"f",0)
        
    #################
    #Stepper Motors
    #################
    #this is only a basic full stepping.
    #speed sets the length of the pulses (and hence the speed...)
    #so is 'backwards' - the fastest that works reliably with the motors I have to hand is 20mS, but slower than that is good. tested to 2000 (2 seconds per step).
    # motor should be 1 or 2 - 1 is terminals for motor 1 and 2 on PCB, 2 is terminals for motor 3 and 4 on PCB

    def step(self,direction, steps, speed =20, holdPosition=False):

        if(direction =="f"):
            directions = ["f", "r"]
            coils = [1,2]
        elif (direction == "r"):
            directions = ["r", "f"]
            coils = [2,1]
        else:
            raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
        while steps > 0: 
            for direction in directions:
                if(steps == 0):
                    break
                for coil in coils:
                    self.motorOn(coil,direction,100)
                    utime.sleep_ms(speed)
                    steps -=1
                    if(steps == 0):
                        break
    #to save power turn off the coils once we have finished.
    #this means the motor wont hold position.
        if(holdPosition == False):            
            for coil in coils:
                self.motorOff(coil)

    #Step an angle. this is limited by the step resolution - so 200 steps is 1.8 degrees per step for instance.
    # a request for 20 degrees with 200 steps/rev will result in 11 steps - or 19.8 rather than 20.
    def stepAngle(self, direction, angle, speed =20, holdPosition=False, stepsPerRev=200):
        steps = int(angle/(360/stepsPerRev))
        print (steps)
        self.step(direction, steps, speed, holdPosition)
        

    #initialisation code for using:
    #defaluts to the standard pins and freq for the kitronik board, but could be overridden
    def __init__(self,Motor1ForwardPin = machine.Pin(3),Motor1ReversePin = machine.Pin(2),Motor2ForwardPin = machine.Pin(6),Motor2ReversePin = machine.Pin(7),PWMFreq = 10000):
        self.motor1Forward=machine.PWM(Motor1ForwardPin)
        self.motor1Reverse=machine.PWM(Motor1ReversePin)
        self.motor2Forward=machine.PWM(Motor2ForwardPin)
        self.motor2Reverse=machine.PWM(Motor2ReversePin)
        self.motor1Forward.freq(PWMFreq)
        self.motor1Reverse.freq(PWMFreq)
        self.motor2Forward.freq(PWMFreq)
        self.motor2Reverse.freq(PWMFreq)

         
