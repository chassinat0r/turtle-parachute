import turtle, math

# Bullet object
class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self): # Draw bullet
        # Go to co-ordinates of bullet
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()

        turtle.setheading(0)
        turtle.right(self.angle - 90) # Set angle of bullet based on turret
        turtle.width(2) # Make lines thicker
        turtle.forward(15)
        turtle.width(1) # Revert

    def move(self): # Move bullet
        # Use cos + sin functions to calculate change in X and Y
        self.x += math.cos(math.radians(90 - self.angle)) * 0.2
        self.y += math.sin(math.radians(90 - self.angle)) * 0.2
