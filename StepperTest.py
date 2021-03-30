import PicoMotorDriver
import utime

board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

while True:
        for direction in directions:
            for stepcount in range(50):
                board.step(direction,8)
            utime.sleep_ms(100)
                
                
    
    
