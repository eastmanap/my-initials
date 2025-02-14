# Pygame Template 1.0

# Import the pygame and system modules
import pygame
import sys

# --- Constants --- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60  # Frames per second
WHITE = (255, 255, 255)  # RGB triplet saved in a tuple

# --- Initialize Pygame ---
pygame.init()

# --- Screen setup --- #
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("template name")

# --- Clock setup --- #
clock = pygame.time.Clock()  # Note the capital C in the word Clock!

# --- Game loop --- #
running = True
while running:
    # --- Listen for and handle events --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Type the QUIT event in UPPERCASE!
            running = False

    # --- Game logic --- #
    # (This is where you'll put your game's logic)

    # --- Draw --- #
    screen.fill(WHITE)  # Fill screen background with white

    # (This is where you'll draw your game objects)
    def draw_line(coord1, coord2, color = (0, 0, 0), width = 50):
        pygame.draw.line(screen, color, coord1, coord2, width)

    # Letter A
    draw_line((100, 100), (300, 100), (75, 204, 178))
    draw_line((100, 100), (100, 300), (75, 204, 178))
    draw_line((300, 100), (300, 300), (75, 204, 178))
    draw_line((100, 300), (300, 300), (75, 204, 178))
    draw_line((100, 300), (100, 525), (75, 204, 178))
    draw_line((300, 300), (300, 525), (75, 204, 178))

    # Letter E
    draw_line((500, 100), (700, 100))
    draw_line((500, 100), (500, 300))
    draw_line((500, 300), (700, 300))
    draw_line((500, 300), (500, 500))
    draw_line((500, 500), (700, 500))
    
    pygame.display.flip()  # Update the display

    # --- Limit frames per second (FPS) --- #
    clock.tick(FPS)

# --- Quit Pygame and exit system module --- #
pygame.quit()
sys.exit()
