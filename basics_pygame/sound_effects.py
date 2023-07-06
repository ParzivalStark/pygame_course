import pygame

# Initialize pygame
pygame.init()

# Dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Create a display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

# Title of the window
pygame.display.set_caption("Adding sounds!")

# Load sound effects
sound_1 = pygame.mixer.Sound('basics_pygame/music/sound_1.wav')
sound_2 = pygame.mixer.Sound('basics_pygame/music/sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# Change the volum of a sound effect
sound_2.set_volume(0.1)
sound_2.play()

# Load background music
pygame.mixer.music.load('basics_pygame/music/music.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()


# Main game loop
running = True
while running:
    # Check the events that have happened
    for event in pygame.event.get():
        # Check if close window button was pressed
        if event.type == pygame.QUIT:
            # End main loop
            running = False

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()