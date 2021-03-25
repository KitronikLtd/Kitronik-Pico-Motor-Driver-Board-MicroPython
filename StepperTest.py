import PicoMotorDriver
import utime

board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

while True:
        for direction in directions:
             for stepcount in range(200):
                board.step(1,direction,8)
                
    
    
