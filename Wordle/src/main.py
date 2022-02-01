import pygame
import state
import drawing
import time

pygame.init()

# constants
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h - 50) # full screen
SCREEN_SIZE = (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 1.5) # half screen
GRID_AREA = (int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 1.75))
WORD_AREA = (2 * int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 1.75))
BG_COLOR = (220, 220, 220)
FONT = pygame.freetype.SysFont("Times New Roman", 0)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Wordle")
pygame.display.set_icon(pygame.image.load('../assets/green w.png'))



running = True
state = state.State()

tick = time.time()
while running:
    if time.time() - tick < 0.0166666: # 60 fps
        continue
    else:
        tick = time.time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if 97 <= event.key <= 122: # a through z
                state.add_key(chr(event.key))
            elif event.key == 8 or event.key == 127:
                state.delete_key()
            elif event.key == 13:
                state.make_guess()
            # print(event.key)
    screen.fill(BG_COLOR)
    
    drawing.draw_grid(screen, FONT, state, GRID_AREA)
    drawing.draw_letters(screen, FONT, state, WORD_AREA)

    pygame.display.update()


