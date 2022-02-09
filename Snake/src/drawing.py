import pygame

pygame.init()

EMPTY_COLOR = (0, 0, 0)
SNAKE_COLOR = (90, 200, 0)
FOOD_COLOR = (240, 0, 0)
DEAD_COLOR = (255, 255, 255)
BG_COLOR = (100, 100, 100)
TEXT_COLOR = (0, 0, 0)

def draw_grid(screen, state, grid_area):
    rows, cols = state.rows, state.cols
    grid_left, grid_top, grid_width, grid_height = grid_area
    square_width = min(grid_height // rows, grid_width // cols)
    grid_left = grid_left + (grid_width - square_width * cols) / 2
    grid_top = grid_top + (grid_height - square_width * rows) / 2
    state.drawing_left = grid_left
    state.drawing_width = square_width * cols
    def pos(x, y):
        return (grid_left + x * square_width, grid_top + y * square_width, square_width, square_width)
    for row in range(rows):
        for col in range(cols):
            if state.grid[row][col] == 'S':
                color = SNAKE_COLOR
            elif state.grid[row][col] == 'F':
                color = FOOD_COLOR
            elif state.grid[row][col] == 'D':
                color = DEAD_COLOR
            else:
                color = EMPTY_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(pos(col, row)), 0)

def draw_score(screen, font, state, text_area):
    TEXT_RATIO = 35
    text_size = text_area[2] // TEXT_RATIO
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(text_area), 0)
    text = "SCORE: " + str(state.size)
    text_rect = font.get_rect(text, size = text_size)
    text_rect.topleft = pygame.Rect(text_area).topleft
    text_rect.left = state.drawing_left
    font.render_to(screen, text_rect, text, TEXT_COLOR, size = text_size)
    if state.dead:
        text = "Game Over. Press ENTER to restart."
        text_rect = font.get_rect(text, size = text_size)
        text_rect.topleft = pygame.Rect(text_area).topleft
        text_rect.right = state.drawing_left + state.drawing_width
        font.render_to(screen, text_rect, text, TEXT_COLOR, size = text_size)