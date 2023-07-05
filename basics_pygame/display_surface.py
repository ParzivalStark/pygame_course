import pygame

# Initialize pygame
pygame.init()

# Dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title of the window
pygame.display.set_caption("Hello World!")

# Main game loop
running = True
while running:
    # Check the events that have happened
    for event in pygame.event.get():
        print(event)
        # Check if close window button was pressed
        if event.type == pygame.QUIT:
            # End main loop
            running = False

# End the game
pygame.quit()