import pygame
pygame.init() # to initialize pygame, it returns a value and to see the returned value we can store it in a variable

# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Flappy Bird") # to set title of window

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop (because the window gets closed automatically so to stop it we create a game loop)
while not exit_game:
    # Handling events
    for event in pygame.event.get():  # pygame.event.get() contains all the event that we perform
        # print(event) 

        # to handle quit event
        if event.type == pygame.QUIT:
            exit_game = True

        # to handle button press event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key.")


                
pygame.quit() # this is for quiting pygame
quit() # this is for quiting python