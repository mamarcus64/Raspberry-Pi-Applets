import pygame
import state
import drawing
import time
from pygame import freetype

pygame.init()

# constants
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h - 50) # full screen
# SCREEN_SIZE = (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 1.5) # half screen
GRID_AREA = (int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 1.75))
WORD_AREA = (2 * int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 1.75))
BUTTON_AREA = (0, int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] / 3), int(SCREEN_SIZE[1] / 1.75))
BG_COLOR = (220, 220, 220)
FONT = pygame.freetype.SysFont("Times New Roman", 0)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Wordle")
pygame.display.set_icon(pygame.image.load('../assets/green w.png'))

left_area_left, left_area_top, left_area_width, left_area_height = BUTTON_AREA
button_width, button_height = left_area_width // 3, left_area_height // 10
button_four = (left_area_left + left_area_width // 2  - button_width // 2, left_area_top + 2 * button_height, button_width, button_height)
button_five = (left_area_left + left_area_width // 2  - button_width // 2, left_area_top + 4 * button_height, button_width, button_height)
button_six = (left_area_left + left_area_width // 2  - button_width // 2, left_area_top + 6 * button_height, button_width, button_height)

running = True
game_state = state.State()

tick = time.time()
while running:
    if time.time() - tick < 0.0166666: # 60 fps
        continue
    else:
        tick = time.time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if button_four[0] <= mouse[0] <= button_four[0] + button_four[2] and button_four[1] <= mouse[1] <= button_four[1] + button_four[3]:
                game_state = state.State(rows=6, cols=4)
                break
            if button_five[0] <= mouse[0] <= button_five[0] + button_five[2] and button_five[1] <= mouse[1] <= button_five[1] + button_five[3]:
                game_state = state.State(rows=6, cols=5)
                break
            if button_six[0] <= mouse[0] <= button_six[0] + button_six[2] and button_six[1] <= mouse[1] <= button_six[1] + button_six[3]:
                game_state = state.State(rows=6, cols=6)
                break
        if event.type == pygame.QUIT:
            running = False
        elif game_state.guess == game_state.word and event.type == pygame.KEYUP and event.key == 13:
            game_state = state.State(rows=game_state.rows, cols=game_state.cols)
            break
        elif game_state.guess == game_state.word:
            continue
        elif game_state.current_row == game_state.rows and event.type == pygame.KEYUP:
            game_state = state.State(rows=game_state.rows, cols=game_state.cols)
            break
        elif event.type == pygame.KEYUP:
            if 97 <= event.key <= 122: # a through z
                game_state.add_key(chr(event.key))
            elif event.key == 8 or event.key == 127:
                game_state.delete_key()
            elif event.key == 13:
                game_state.make_guess()
    screen.fill(BG_COLOR)
    
    drawing.draw_grid(screen, FONT, game_state, GRID_AREA)
    drawing.draw_letters(screen, FONT, game_state, WORD_AREA)
    drawing.draw_button(screen, FONT, button_four, "4-letter restart")
    drawing.draw_button(screen, FONT, button_five, "5-letter restart")
    drawing.draw_button(screen, FONT, button_six, "6-letter restart")
    if game_state.current_row == game_state.rows or game_state.guess == game_state.word:
        final_area = (GRID_AREA[0] + GRID_AREA[2] // 2 - GRID_AREA[0] // 8, GRID_AREA[1] + GRID_AREA[3], GRID_AREA[0] // 3, GRID_AREA[0] // 4)
        drawing.draw_button(screen, FONT, final_area, "Word: " + game_state.word,  color=BG_COLOR)

    pygame.display.update()


