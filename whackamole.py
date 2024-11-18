import pygame
import random

def draw_grid(screen, rows, cols, square_size, color):
    for row in range(rows + 1):
        pygame.draw.line(screen, color, (0, row * square_size), (cols * square_size, row * square_size))
    for col in range(cols + 1):
        pygame.draw.line(screen, color, (col * square_size, 0), (col * square_size, rows * square_size))

def get_random_position(rows, cols, square_size):
    random_row = random.randrange(0, rows)
    random_col = random.randrange(0, cols)
    return random_col * square_size, random_row * square_size

# this is my first
def main():
    try:
        pygame.init()
        square_size = 32
        cols = 20
        rows = 16
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_position = (0, 0)
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_position, (square_size, square_size))
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_position = get_random_position(rows, cols, square_size)

            screen.fill("light green")
            draw_grid(screen, rows, cols, square_size, "dark blue")
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
