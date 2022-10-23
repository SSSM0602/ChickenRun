class pipe(object):
    def __init__(self):
        pass
    
    def create(self, position, gap):
        pushMatrix()
        translate(position,0,0)
        
        #bottom pipe head, tail
        pushMatrix()
        translate(0, gap, 0) # BOTTOM POSITION
        
        pushMatrix()
        rotateX(radians(90))
        scale(9,9,3)
        fill (56, 10, 20) #green
        cylinder()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        scale(8,8,50)
        translate(0,0,-1)
        fill (56, 10, 20) #green
        cylinder()
        popMatrix()
        
        popMatrix()
        
        #top pipe head, tail
        pushMatrix()
        translate(0, gap - 20 ,0) # TOP POSITION
        
        pushMatrix()
        rotateX(radians(90))
        scale(9,9,3)
        translate(0,0,16)
        fill (56, 10, 20) #green0
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        scale(8,8,50)
        translate(0,0,2)
        fill (56, 10, 20) #green
        cylinder()
        popMatrix()
        
        popMatrix()
        
        popMatrix()


# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
