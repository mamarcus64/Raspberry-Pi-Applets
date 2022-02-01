import pygame

pygame.init()

TEXT_COLOR = (0, 0, 0)
BLANK_SQUARE_COLOR = (134, 134, 134)
GUESS_SQUARE_COLOR = (70, 70, 70)
YELLOW_SQUARE_COLOR = (235, 210, 0)
GREEN_SQUARE_COLOR = (90, 200, 0)
BORDER_RATIO = 23.5
TEXT_SIZE_RATIO = 1.25

def draw_grid(screen, font, state, grid_area):
    vert_spacing_ratio = 0.15
    hor_spacing_ratio = 0.15
    shake_row, shake_frame = state.shake
    if shake_row != -1:
        if shake_frame >= 32:
            state.shake = (-1, -1)
        else:
            state.shake = (shake_row, shake_frame + 1)
    rows, cols = state.rows, state.cols
    grid_left, grid_top = grid_area[0], grid_area[1]
    grid_width, grid_height = grid_area[2], grid_area[3]
    square_width = int(grid_height / (rows + (rows - 1) * vert_spacing_ratio))
    vert_spacing = int(square_width * vert_spacing_ratio)
    hor_spacing = square_width * hor_spacing_ratio
    shake_width = square_width / 30
    grid_left = int(grid_left + (grid_width - (cols * square_width + (cols - 1) * hor_spacing)) / 2)

    def shake_offset(frame):
        frame = frame % 8
        if frame == 0 or frame == 4: offset = 0
        if frame == 1 or frame == 3: offset = 1
        if frame == 2: offset = 2
        if frame == 5 or frame == 7: offset = -1
        if frame == 6: offset = -2
        return offset * shake_width

    def calc_position(x, y, dx=0, dy=0):
        return (grid_left + x * (square_width + hor_spacing) + dx, grid_top + y * (square_width + vert_spacing) + dy, square_width, square_width)
    for row in range(rows):
        for col in range(cols):
            if not state.board[row][col]:
                pygame.draw.rect(screen, BLANK_SQUARE_COLOR, pygame.Rect(calc_position(col, row)), int(square_width / BORDER_RATIO))
            else:
                
                text, type = state.board[row][col]
                if type == 'right': color = GREEN_SQUARE_COLOR
                elif type == 'half-right': color = YELLOW_SQUARE_COLOR
                elif type == 'wrong': color = BLANK_SQUARE_COLOR
                elif type == 'guess': color = GUESS_SQUARE_COLOR

                rect = pygame.Rect(calc_position(col, row, dx = shake_offset(shake_frame) if row == shake_row else 0))
                pygame.draw.rect(screen, color, rect, square_width if type != 'guess' else int(square_width / BORDER_RATIO))
                text_rect = font.get_rect(text, size = square_width / TEXT_SIZE_RATIO)
                text_rect.center = pygame.Rect(calc_position(col, row)).center
                font.render_to(screen, text_rect, text, TEXT_COLOR, size = square_width / TEXT_SIZE_RATIO)

def draw_letters(screen, font, state, word_area):
    vert_spacing_ratio = 0.15
    hor_spacing_ratio = 0.15
    rows, cols = 7, 4
    word_left, word_top = word_area[0], word_area[1]
    word_width, word_height = word_area[2], word_area[3]
    square_width = int(word_height / (rows + (rows - 1) * vert_spacing_ratio))
    vert_spacing = int(square_width * vert_spacing_ratio)
    hor_spacing = square_width * hor_spacing_ratio
    word_left = int(word_left + (word_width - (cols * square_width + (cols - 1) * hor_spacing)) / 2)
    def calc_position(x, y):
        return (word_left + x * (square_width + hor_spacing), word_top + y * (square_width + vert_spacing), square_width, square_width)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(26):
        row, col = i // 4, i % 4
        letter = alphabet[i]
        if letter not in state.guessed_letters:
            pygame.draw.rect(screen, BLANK_SQUARE_COLOR, pygame.Rect(calc_position(col, row)), int(square_width / BORDER_RATIO))
        else:
            if state.guessed_letters[letter] == 'right':
                color = GREEN_SQUARE_COLOR
            elif state.guessed_letters[letter] == 'half-right':
                color = YELLOW_SQUARE_COLOR
            else:
                color = BLANK_SQUARE_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(calc_position(col, row)), square_width)
        text_rect = font.get_rect(letter, size = square_width / TEXT_SIZE_RATIO)
        text_rect.center = pygame.Rect(calc_position(col, row)).center
        font.render_to(screen, text_rect, letter, TEXT_COLOR, size = square_width / TEXT_SIZE_RATIO)
