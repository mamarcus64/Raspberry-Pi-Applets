import pygame
import state
import drawing
import time
from pygame import freetype

pygame.init()

# constants
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h - 50) # full screen
# SCREEN_SIZE = (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 1.5) # half screen
PLAY_AREA = (int(SCREEN_SIZE[0] / 10), int(SCREEN_SIZE[1] / 10), int(SCREEN_SIZE[0] * 8 / 10), int(SCREEN_SIZE[1] * 8 / 10))
TEXT_AREA = (int(SCREEN_SIZE[0] / 9), int(SCREEN_SIZE[1] * 9 / 10), int(SCREEN_SIZE[0] * 8 / 10), int(SCREEN_SIZE[1] * 1 / 10))
BG_COLOR = (100, 100, 100)
screen = pygame.display.set_mode(SCREEN_SIZE)
FONT = pygame.freetype.SysFont("Times New Roman", 0)

pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load('../assets/snake.png'))

running = True
game_state = state.State()

tick = time.time()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state.dead and event.key == pygame.K_RETURN:
                game_state = state.State()
                break
            if not game_state.chosen_direction:
                if game_state.direction not in ['left', 'right'] and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game_state.direction = 'right'
                    game_state.chosen_direction = True
                    break
                if game_state.direction not in ['left', 'right'] and event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game_state.direction = 'left'
                    game_state.chosen_direction = True
                    break
                if game_state.direction not in ['down', 'up'] and event.key == pygame.K_UP or event.key == pygame.K_w:
                    game_state.direction = 'up'
                    game_state.chosen_direction = True
                    break
                if game_state.direction not in ['down', 'up'] and event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game_state.direction = 'down'
                    game_state.chosen_direction = True
                    break
            else:
                if game_state.direction not in ['left', 'right'] and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game_state.direction_buffer = 'right'
                    break
                if game_state.direction not in ['left', 'right'] and event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game_state.direction_buffer = 'left'
                    break
                if game_state.direction not in ['down', 'up'] and event.key == pygame.K_UP or event.key == pygame.K_w:
                    game_state.direction_buffer = 'up'
                    break
                if game_state.direction not in ['down', 'up'] and event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game_state.direction_buffer = 'down'
                    break

    if time.time() - tick < 0.0166666: # 60 fps
        continue
    else:
        tick = time.time()

    screen.fill(BG_COLOR)
    if not game_state.dead:
        game_state.move()
    drawing.draw_grid(screen, game_state, PLAY_AREA)
    drawing.draw_score(screen, FONT, game_state, TEXT_AREA)
    pygame.display.update()


