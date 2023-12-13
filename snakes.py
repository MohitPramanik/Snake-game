import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snakes Game")
pygame.display.update()  # if you change anything in your display then you must have to use this function to see the change

# Game specific varaibles
exit_game = False
game_over = False
snake_x = 45 # these define initial position of our snake
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width-20)
food_y = random.randint(20, screen_height-20)
score = 0
init_velocity = 10
snake_size  = 10 # this define initial size of our snake
fps = 30

clock = pygame.time.Clock() # we are creating this because we have to update the frame according to time

font = pygame.font.SysFont(None, 55) # (font-type, font-size)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y]) # this will update the screen

snk_list = []
snk_length = 1

# Game loop
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        # this will control the button press event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # snake_x = snake_x + 10 
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                # snake_x = snake_x - 10
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                # snake_y = snake_y - 10
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                # snake_y = snake_y + 10
                velocity_y = init_velocity
                velocity_x = 0

    # this will enable the snake to move continuously
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score += 1
        # this will change food position once it gets eated
        food_x = random.randint(20, screen_width-20)
        food_y = random.randint(20, screen_height-20)
        snk_length += 5
    

    gameWindow.fill(white) # filling the display with white color and we have to define the colors
    text_screen("Score: " + str(score * 10), red, 5, 5) # this will display score on the screen
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size]) # Creating food for snake

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)


    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size]) # Creating head of our snake (to place inside, color, [position x, position y, width, height])
    pygame.display.update() 
    clock.tick(fps) # we are passing frames per second in this
    