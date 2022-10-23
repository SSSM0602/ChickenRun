

from __future__ import division
import traceback
from pipe import pipe

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view

    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.05
        
        #moves camera away, moves camera up/down, moves camera forward/backward
        if (time < 20):
            camera (100 -time * 5, -50, 100, 0, 0, 0, 0,  1, 0)
        elif (time < 60):
            camera (0, time * -2, 400-time * 5, time * 5, 0, 0, 0,  1, 0)
        elif (time < 100):
            camera (400 + time * -3, (time - 60) * -2, 300, 200, 0, 0, 0,  1, 0)
        elif (time < 137):
            camera (100, 0, 200 + (time - 100) * 3, 400, 0, 0, 0, 1, 0)
        else:
            camera (100, 0, 200 + (137 - 100) * 3, 400, 0, 0, 0,  1, 0)

        background (time*20%255, time*40%255, time*60%255) #light blue
        
        # lights
        #spotLight(51, 102, 126, 80, 20, 40, -1, 0, 0, PI/2, 2)
        # spotLight(51, 102, 126, 0, 0, 0, -1, 0, 0, PI/2, 2)
        lightSpecular(255, 255, 255)
        # directionalLight (100, 100, 100, -0.3, 0.5, -1)
        # directionalLight (-100, 100, -700, -0.3, 0.5, 1)
        #ambientLight(1,1,1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (100.0)
            
        # Time-dependent chicken movements
        pushMatrix()
        scale(0.2,0.2,0.8)
        
        
        if (time < 10):
            translate((time - 3)*20 - 300, 200, 0) # walk on ground
        elif (time < 20):
            translate((time - 3)*20 - 300, 200 - time*25 + 250,0) # fly to pipe
        elif (time < 30):
            translate((time - 3)*20 - 300, -49 + sin(time*10)*5, 0) # hover above pipe
        elif (time < 40):
            translate((time - 3)*20 - 300, -49 - (time - 30)*25, 0) # fly to pipe
        elif (time < 55):
            translate((time - 3)*20 - 300, -300 + sin(time*10)*5, 0) # hover above pipe
        elif (time < 67):
            translate((time - 3)*20 - 300, -300 + (time - 55)*25, 0) # fly to pipe
        elif (time < 80):
            translate((time - 3)*20 - 300, -2.5 + sin(time*10)*5, 0) # hover above pipe
        elif (time < 85):
            translate((time - 3)*20 - 300, -2.5 - (time - 80)*10, 0) # fly to pipe
        elif (time < 100):
            translate((time - 3)*20 - 300, -52.5 + sin(time*10)*5, 0) # hover above pipe
        elif (time < 110):
            translate((time - 3)*20 - 300, -52.5 - (time - 100)*20, 0) # fly to pipe
        elif (time < 133):
            translate((time - 3)*20 - 300, -252.5 + sin(time*10)*5, 0)
        elif (time < 160):
            translate((133 - 3)*20 - 300, -300 + (time-133)*20, 0)
            rotateZ(radians(-90))
        else:
            translate((133 - 3)*20 - 300, -300 + (160-133)*20, 0)
            textSize(300);
            text("Game Over", -1000, 180, 200) 
            fill(0)
            
            #translate(1000,1000,1000) # move away
            
        rotateY(radians(90))
        
        # -----------------------
        # Head Begin
        pushMatrix()
        
        # Head
        pushMatrix()
        fill (255, 255, 255) #white
        scale(1,1,1)
        box(30)
        popMatrix()
        
        # Beak
        pushMatrix()
        fill (255, 165, 0) #orange
        scale(0.9,0.3,0.8)
        translate (0, -15, 15)
        box(30)
        popMatrix()
        
        # Wattles
        pushMatrix()
        fill (255, 0, 0) #red
        scale(0.4,0.4,0.7)
        translate (0, 0, 15)
        box(30)
        popMatrix()
        
        # Comb
        pushMatrix()
        rotateX(radians(10))
        fill (255, 0, 0) #red
        scale(0.2,0.7,0.9)
        translate (0, -30, 3)
        box(30)
        popMatrix()
        
        # Eyes
        pushMatrix()
        fill (0, 0, 0) #black
        scale(0.2,0.2,0.2)
        
        pushMatrix()
        translate (50, -70, 70)
        sphere(20)
        popMatrix()
        
        translate (-50, -70, 70)
        sphere(20)
        popMatrix()
        
        # Head End
        popMatrix()
 
        # Body
        pushMatrix()
        fill (255, 255, 255) #white
        scale(2,1.7,2)
        translate (0, 20, -15)
        box(30)
        popMatrix()
        
        # Wings
        pushMatrix()
        fill (255, 255, 255) #white
        
        pushMatrix()
        
        #ANIMATE WINGS
        if (time < 10):
            rotateZ(radians(-1 * sin(time * 10)*5 + 30))
        elif time < 133:
            rotateZ(radians(abs(cos(time * 10))*90 + 30))
            translate(40,0,0)
        else:
            pass

        translate (-19, 45, -25)
        scale(0.2,1.5,1.5)
        box(30)
        popMatrix()
        
        if (time < 10):
            rotateZ(radians(sin(time * 10)*5 - 30))
        elif time < 133:
            rotateZ(-1 * radians(abs(cos(time * 10))*90 + 30))
            translate(-40,0,0)
        else:
            pass
        
        translate (19, 45, -25)
        scale(0.2,1.5,1.5)
        box(30)
        popMatrix()
        
        # -----------------------
        # Leg 1 Begin 
        pushMatrix()
        
        #ANIMATE WALK
        if (time < 10):
            rotateX(radians(10 * sin(time * 10)))
        else:
            rotateX(radians(-20))
        
        # Leg
        pushMatrix()
        fill (255, 255, 0) #yellow
        scale(0.3,1.4,0.3)
        translate (50, 50, -120)
        box(30)
        popMatrix()
        
        #Feet
        pushMatrix()
        fill (255, 165, 0) #orange
        scale(0.7,0.2,0.7)
        translate (21, 450, -45)
        box(30)
        popMatrix()
        
        #Toe
        pushMatrix()
        fill (255, 165, 0) #orange
        scale(0.3,0.2,0.3)
        translate (50, 450, -60)
        box(30)
        popMatrix()
        
        #Leg 1 End
        popMatrix()
        
        pushMatrix()
        
        #Walking Animation
        if (time < 10):
            rotateX(radians(-10 * sin(time * 10)))
        else:
            rotateX(radians(-20))
        
        # Leg
        pushMatrix()
        fill (255, 255, 0) #yellow
        scale(0.3,1.4,0.3)
        translate (-50, 50, -120)
        box(30)
        popMatrix()
        
        # Feet
        pushMatrix()
        fill (255, 165, 0) #orange
        scale(0.7,0.2,0.7)
        translate (-21, 450, -45)
        box(30)
        popMatrix()
        
        # Toe
        pushMatrix()
        fill (255, 165, 0) #orange
        scale(0.3,0.2,0.3)
        translate (-50, 450, -60)
        box(30)
        popMatrix()
        
        # Leg 2 End
        popMatrix()
        
        #Instantiate Pipes in World
        popMatrix()
        
        # Pipes range: -30 to 50
        pipes = pipe()
        pipes.create(40, 20)
        pipes.create(130, -30)
        pipes.create(210, 40)
        pipes.create(300, 30)
        pipes.create(390, -10)
        pipes.create(480, 45)
        pipes.create(570, -10)
        pipes.create(660, -20)
        pipes.create(750, 40)
        pipes.create(840, 30)
        pipes.create(930, -30)
    
        platform()
        
    except Exception:
        traceback.print_exc()

def platform():
    pushMatrix()
    fill (0, 255, 0) #green
    scale(100,0.2,8)
    translate(0,320,0)
    box(30)
    popMatrix()
    
    pushMatrix()
    fill (181, 101, 30) #brown
    scale(100,5,8)
    translate(0,28.4,0)
    box(30)
    popMatrix()
    
    pushMatrix()
    fill (255, 255, 255) #blue
    scale(100,5,8)
    translate(0,-40,0)
    box(30)
    popMatrix()
    
    
