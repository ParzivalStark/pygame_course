import pygame

# Initialize pygame
pygame.init()

# Dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title of the window
pygame.display.set_caption("Drawing Objects")

# Define colors
BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
YELLOW  = (255, 255,   0)
CYAN    = (  0, 255, 255)
MAGENTA = (255,   0, 255)

# Background color for display
display_surface.fill(BLUE)

# Draw some shapes
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 10)

pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2), 200, 10)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2), 191, 0)

pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 75, 250))

# Main game loop
running = True
while running:
    # Check the events that have happened
    for event in pygame.event.get():
        # Check if close window button was pressed
        if event.type == pygame.QUIT:
            # End main loop
            running = False
    
    # Update display
    pygame.display.update()

# End the game
pygame.quit()