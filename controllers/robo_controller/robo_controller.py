from controller import Robot, Keyboard, Motion

timestep=32

robot= Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')
   
def printMessages():
    print('press up to wave')
     
key = -1

printMessages()

while robot.step(timestep) != -1:

    key = keyboard.getKey()  
    
    if key == Keyboard.UP:
        wave.play()
   
