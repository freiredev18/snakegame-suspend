# importing pygame library
import pygame

# That line will inicialize the pygame
pygame.init()

# Defining the limits of the pygame window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# That line create the screen and can be used for images in the window
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT)) #Defining the size of screen resolution using "pygame.display.set_mode"
snake = pygame.Rect((300, 250, 15, 15)) #This line will tell to python where and what is the size of the snake (x, y, width, height)

pygame.display.set_caption('SnakeGame Demo') # That line is just for define the name os the window

# Creating the pygame loop
running = True
while running: #While running is True, do something
    screen.fill((30, 30, 30)) #That line serves to fill the pixels after the snakes pass throght them
    pygame.draw.rect(screen, (144, 238, 144), snake) #Inside the list, have this sequence, 1 - "screen" to indicate for python, that the draw needs to be seened in screen, 2 - inside the second list, is the colors of the snake in the screen, 3 - We teeling for the python as the snake needs to be showed on screen with the current colors
    key = pygame.key.get_pressed() #Defining when the was pressed, python call modulem get_pressed
    if key[pygame.K_UP] == True: #In that line and on the other lines, we are defining all the keys functions, one by one
        snake.move_ip(0, -1) # Defining the cordinates of the skake, when the user press up, X will stay stopped, but the snake will go throught up, because the Y is in -1
    elif key[pygame.K_DOWN] == True:
        snake.move_ip(0, 1)
    elif key[pygame.K_LEFT] == True:
        snake.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        snake.move_ip(1, 0)


    for event in pygame.event.get(): #Checking with for and .get if the user will close the window
        if event.type == pygame.QUIT: #If the type of event that the user do, is quit the game, define running as false, that way the programm gonna close
            running = False 

    pygame.display.update()

pygame.quit() #That line is the opposite of init(), in other words, the quit() os just for close the programm


