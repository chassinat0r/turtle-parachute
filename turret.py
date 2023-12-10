import turtle

# Object to add and turn turret to shoot at targets
class Turret:
    def __init__(self, x, y, radius):
        # Set co-ordinates, radius, diameter, and angle
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = 2 * radius
        self.angle = 0
        self.left = False
        self.right = False

    def draw(self): # Draw turret
        turtle.up()
        turtle.setheading(0)
        turtle.goto(self.x, self.y) # Go to position of turret
        turtle.down()

        turtle.begin_fill() # Whatever is drawn will be filled in
        turtle.circle(self.radius) # Draw a circle of the radius
        turtle.end_fill() # Fill the resultant circle

        turtle.up()

        # Move turtle to centre of circle
        turtle.left(90)
        turtle.forward(self.radius)

        # Move turtle to the left of the circle
        turtle.left(90)
        turtle.forward(self.diameter)

        # Draw rectangle through bottom half of circle
        turtle.right(180) # Face right
        turtle.down() # Start drawing

        turtle.begin_fill()
        
        # Draw outline for rectangle
        for i in range(0, 2):
            turtle.forward(2 * self.diameter)
            turtle.right(90)
            turtle.forward(self.radius)
            turtle.right(90)

        turtle.end_fill() # Fill rectangle

        turtle.width(3)
        turtle.up()
        turtle.goto(self.x, self.y + self.diameter)
        turtle.down()
        turtle.right(self.angle - 90)
        turtle.forward(self.radius)
        turtle.width(1)

    def turnLeft(self): # Turn turret to aim left
        if self.angle > -70: # Angle of turret is more than -70 degrees
            self.angle -= 0.2 # Turn turret 2 degrees to left

    def turnRight(self): # Turn turret to aim right
        if self.angle < 70: # Angle of turret is less than 70 degrees
            self.angle += 0.2 # Turn turret 2 degrees to the right
