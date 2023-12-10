import turtle, math, sys
from turret import Turret
from bullet import Bullet

turtle.title("Parachute") # Give window title
turtle.tracer(0, 0) # Disable auto-update
turtle.hideturtle() # Hide the turtle

# Object to manage the game
class Game:
    def __init__(self, width, height):
        # Set width and height values
        self.width = width
        self.height = height

        self.score = 0

        self.turret = Turret(0, -self.height / 2, 15) # Create turret at bottom middle of screen

        self.bullets = []

        turtle.listen() # Listen for keypress

        # Turn turret left/right when arrow keys pressed
        turtle.onkeypress(self.turret.turnLeft, "Left")
        turtle.onkeypress(self.turret.turnRight, "Right")
        turtle.onkeypress(self.shoot, "space")

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
        while True:
            turtle.clear() # Get rid of everything previously drawn
            
            self.draw() # Draw the screen
            self.turret.draw() # Draw the turret

            bullets_to_delete = [] # List of indexes of bullets to delete that have gone offscreen

            # Go through each bullet looking if they have gone off screen
            for i in range(0, len(self.bullets)):
                bullet = self.bullets[i]

                bullet.move() # Move bullet

                # If bullet has gone outside the X or Y boundaries of the screen
                if abs(bullet.x) + 15 >= self.width / 2 or abs(bullet.y) + 15 >= self.height / 2:
                    bullets_to_delete.append(i - len(bullets_to_delete)) # Add index
                    """Subtract length of bullets to delete list to take
                    into account indexes will change each time a bullet
                    is deleted"""
                else: # Bullet still within boundaries
                    bullet.draw() # Draw bullet

            # Delete bullets that have gone off the screen
            for index in bullets_to_delete:
                self.bullets.pop(index)

            # Display score above screen
            turtle.up()
            turtle.goto(-self.width / 2, self.height / 2)
            turtle.down()
            turtle.write("Score: " + str(self.score))

            turtle.update() # Update turtle

    def shoot(self): # Shoot a bullet
        radians = math.radians(90 - self.turret.angle) # Get angle of triangle in radians

        # Calculate X and Y from the turret
        x = self.turret.x + (math.cos(radians) * self.turret.radius)
        y = self.turret.y + self.turret.diameter + (math.sin(radians) * self.turret.radius)

        # Create bullet and add to list
        bullet = Bullet(x, y, self.turret.angle)
        self.bullets.append(bullet)

game = Game(600, 400) # Create screen for game of size 600x400

try:
    game.update() # Continually refresh the screen
except turtle.Terminator: # Prevent error when closing window
    sys.exit(0) # Exit with no errors
