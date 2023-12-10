import turtle, time, sys
from turret import Turret

turtle.title("Parachute") # Give window title
turtle.tracer(0, 0) # Disable auto-update
turtle.hideturtle() # Hide the turtle

# Object to create the screen the game is played in
class Screen:
    def __init__(self, width, height):
        # Set width and height values
        self.width = width
        self.height = height

        self.turret = Turret(0, -self.height / 2, 15) # Create turret at bottom middle of screen

        turtle.listen() # Listen for keypress

        # Turn turret left/right when arrow keys pressed
        turtle.onkeypress(self.turret.turnLeft, "Left")
        turtle.onkeypress(self.turret.turnRight, "Right")

    def draw(self): # Render the screen in the window
        turtle.up() # Stop drawing
        turtle.setheading(0) # Reset angle
        turtle.goto(-self.width / 2, self.height / 2) # Go to position of what will be the top left corner of screen
        turtle.down() # Start drawing
        
        for i in range(0, 2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)

    def update(self): # Update the game
        turtle.clear() # Get rid of everything previously drawn
        
        self.draw() # Draw the screen
        self.turret.draw() # Draw the turret

        turtle.update() # Update turtle

        # Repeat in 1 second
        time.sleep(0.1) 
        self.update()

screen = Screen(600, 400) # Create screen of size 600x400

try:
    screen.update()
except turtle.Terminator: # Prevent error when closing window
    sys.exit(0) # Exit with no errors
