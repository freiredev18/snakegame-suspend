#Importing pygame library
import pygame

#Initializating pygame
pygame.init()

#Defining the size window
screen = pygame.display.set_mode((800, 600))

#That line will create a 'clock', what for us, is just the FPS counter
clock = pygame.time.Clock()

#Some colors
olivegreen = (140, 165, 110)
snakecolor = (30, 60, 20)

#Snake body separete by segments
snake = [
    pygame.Rect(400, 300, 20, 20),
    pygame.Rect(480, 380, 20, 20),
    pygame.Rect(460, 360, 20, 20)
]

dir = [0, 0]

#Running the loops that will keep the games alive
running = True
while running:

    #Fill the screen with a color to wipe away from last frame
    screen.fill(olivegreen)

    #Creating the movement of snake, a new head is create and inserted in index 0 of snakes body
    snakehead = snake[0].copy()
    snakehead.move_ip(dir)
    snake.insert(0, snakehead)
    snake.pop()

    #Drawning the snake in screen
    pygame.draw.rect(screen, snakecolor, snake[0])
    pygame.draw.rect(screen, snakecolor, snake[1])
    pygame.draw.rect(screen, snakecolor, snake[2])

    #Snakes move infinite
    snake[0].move_ip(dir)
    snake[1].move_ip(dir)
    snake[2].move_ip(dir)

    #Deifining if the user press quit, the program will close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #KEYDOWN is a command like "When pressed"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = [0, -20]
            if event.key == pygame.K_DOWN:
                dir = [0, 20]
            if event.key == pygame.K_LEFT:
                dir = [-20, 0]
            if event.key == pygame.K_RIGHT:
                dir = [20, 0]

    #To update the display and show the events on the screen
    pygame.display.flip()

    #Defining the 'FPS'
    clock.tick(10)

#For quit the game
pygame.quit()