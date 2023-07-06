import pygame

# Initialize pygame
pygame.init()

# Dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title of the window
pygame.display.set_caption("Blitting text")

# Define colors
BLACK     = (  0,   0,   0)
DARKGREEN = ( 10,  50,   0)
GREEN     = (  0, 255,   0)

# See all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# Define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('basics_pygame/fonts/AttackGraffiti.ttf', 32)

# Define text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

# Main game loop
running = True
while running:
    # Check the events that have happened
    for event in pygame.event.get():
        # Check if close window button was pressed
        if event.type == pygame.QUIT:
            # End main loop
            running = False
    
    # Blit the text surfaces to the display
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()