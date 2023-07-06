import pygame

# Initialize pygame
pygame.init()

# Dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title of the window
pygame.display.set_caption("Blitting images")

# Create images
dragon_left_image = pygame.image.load("basics_pygame/images/dragon_left.png")
dragon_left_rect  = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("basics_pygame/images/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

# Main game loop
running = True
while running:
    # Check the events that have happened
    for event in pygame.event.get():
        # Check if close window button was pressed
        if event.type == pygame.QUIT:
            # End main loop
            running = False
    # Blit a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (50,100,200), (0,70), (WINDOW_WIDTH,70), 5)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()