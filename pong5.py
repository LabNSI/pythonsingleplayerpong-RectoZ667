import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(BLACK)
pygame.display.update()

radius = 10
x = WIDTH//2
y = radius

pygame.draw.circle(screen, WHITE, (x,y), radius)  # Position is the center of the circle.


paddle = { "width" : 200,
           "height": 20,
           "color" : BLUE,
           "x"     : 0,
           "y"     : 0}
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]
pygame.draw.rect(sreen, BLUE, (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 5
x_sens = y_sens = 1
pause = False


end = False
while not end:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = True

    if key[pygame.K_RETURN]:
        pause = False

    if key[pygame.K_m]:
        auto = False

    if not pause:

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            paddle["x"] = paddle["x"] + speed
						if paddle["x"]<0:
							x= 0

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            paddle["x"] = paddle["x"] + speed
						if paddle["x"]> WIDTH - paddle["width"]:
							paddle["x"] = WIDTH - paddle["width"]

        # change x direction if the ball hits the left or right edge
        if x < radius or x > WIDTH - radius:
					x_sens = -x_sens

        # change y direction if the ball hits the top edge
        if y < radius:
					y_sens = -y_sens

         # if the ball hits the paddle top
        if y > HEIGHT - paddle["height"]
					y_sens = -y_sens
            # if the ball is between the x paddle begin and the x paddle end
            if x > paddle("x") and x < paddle["width"] + paddle["x"]:
                # change y direction
                y_sens = -y_sens

        # if the ball comes out of the screen from below, end the game
        ???

        # compute the new ball coordinates
        x = x + x_sens * speed
        y = y + y_sens * speed

    # redraw ball and paddle
    pygame.draw.circle(screen, WHITE, (x, y), radius)
    pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    # update screen
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()