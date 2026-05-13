# importing pygame library
import pygame

# That line will inicialize the pygame
pygame.init()

# Defining the limits of the pygame window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# That line create the screen and can be used for images in the window
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT)) #Defining the size of screen resolution using "pygame.display.set_mode"
snake = [ #This line will tell to python where and what is the size of the snake (x, y, width, height)
    pygame.Rect(600, 300, 25, 25), 
    pygame.Rect(580, 300, 25, 25),
    pygame.Rect(560, 300, 25, 25)
] 

clock = pygame.time.Clock() # This "builds" the clock object

pygame.display.set_caption('SnakeGame Demo') # That line is just for define the name os the window

# Creating the pygame loop
running = True

while running: #While running is True, do something

    screen.fill((30, 30, 30)) #That line serves to fill the pixels after the snakes pass throght them
    direction = (0, 0) #That variable will serve to save the cordinates of x and y in a tuple, and will be used on pygame.K, the direction will subistitute the native direction
    for segment in snake: #Telling to python, you must have show one of each segment of the snake, in other words, one by one
        pygame.draw.rect(screen, (144, 238, 144), segment) #Inside the list, have this sequence, 1 - "screen" to indicate for python, that the draw needs to be seened in screen, 2 - inside the second list, is the colors of the snake in the screen, 3 - We teeling for the python as the snake needs to be showed on screen with the current colors

    key = pygame.key.get_pressed() #Defining when the was pressed, python call modulem get_pressed
    if key[pygame.K_UP]:    direction = (0, -25) #This line is a command to define the positioon of x and y based on especific key pressed
    if key[pygame.K_DOWN]:  direction = (0, 25)
    if key[pygame.K_LEFT]:  direction = (-25, 0)
    if key[pygame.K_RIGHT]: direction = (25, 0)

    if direction != (0, 0): #New condition for the moves using for
        # Create a new head based on the current heads position
        new_head = snake[0].copy() #This will copy the head of the snake, in other words, copy the 0 index in list
        new_head.move_ip(direction) #This gonna movie the head based on direction
        
        # Add new head to start, remove the last tail piece
        snake.insert(0, new_head) #Using insert for add in index 0 a new_head
        snake.pop() #Used to delet the rest of the tail

    head = snake[0] #Defining the head of the snake
    #Defining that if the head hits top, right, or the other limits of the window, the game gonna stop
    if head.left < 0 or head.right > SCREEN_WIDTH or head.top < 0 or head.bottom > SCREEN_HEIGHT:
        snake = [ 
    pygame.Rect(600, 300, 25, 25), 
    pygame.Rect(580, 300, 25, 25),
    pygame.Rect(560, 300, 25, 25)
] 
        direction = (600, 300)

    for event in pygame.event.get(): #Checking with for and .get if the user will close the window
        if event.type == pygame.QUIT: #If the type of event that the user do, is quit the game, define running as false, that way the programm gonna close
            running = False #Stopping game

    pygame.display.update() #Used to update the display all the time
    clock.tick(10) #Limiting FPS by 10

pygame.quit() #That line is the opposite of init(), in other words, the quit() os just for close the programm


