import random

class State:
    def __init__(self, rows = 30, cols = 40):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for col in range(cols)] for row in range(rows)]
        self.head = (self.rows // 4 + random.randint(0, self.rows // 2), self.cols // 4 + random.randint(0, self.cols // 2))
        self.snake = [self.head]
        self.generate_food()
        self.direction = None
        self.direction_buffer = None
        self.chosen_direction = False
        self.frame = 0
        self.speed = 5 # number of frames per movement
        self.food_count = 0
        self.dead = None
        self.wrap_around = False
        self.size = 1
        self.drawing_left = -1
        self.drawing_width = -1
        self.update_grid()

    def update_grid(self):
        self.grid = [[None for col in range(self.cols)] for row in range(self.rows)]
        for body in self.snake:
            self.grid[body[0]][body[1]] = 'S'
        self.grid[self.food[0]][self.food[1]] = 'F'
        if self.dead:
            self.grid[self.dead[0]][self.dead[1]] = 'D'
    
    def generate_food(self):
        self.food = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        while self.food in self.snake:
            self.food = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))

    def move(self):

        self.frame += 1
        if self.frame > 0 and self.frame % self.speed == 0:
            self.frame = 0
            self.chosen_direction = False
            if self.direction == 'right':
                self.head = (self.head[0], self.head[1] + 1)
            elif self.direction == 'left':
                self.head = (self.head[0], self.head[1] - 1)
            elif self.direction == 'up':
                self.head = (self.head[0] - 1, self.head[1])
            elif self.direction == 'down':
                self.head = (self.head[0] + 1, self.head[1])
            if self.wrap_around:
                self.head = (self.head[0] % self.rows, self.head[1] % self.cols)
            if self.head == self.food:
                self.food_count += 4
                self.generate_food()
            if self.food_count == 0:
                popped = self.snake.pop()
            else:
                popped = self.snake[0]
                self.size += 1
                self.food_count -= 1
            if self.head in self.snake:
                self.snake.insert(len(self.snake), popped)
                self.dead = self.head
                self.direction = None
            elif self.head[0] < 0 or self.head[0] >= self.rows or self.head[1] < 0 or self.head[1] >= self.cols:
                self.snake.insert(len(self.snake), popped)
                self.dead = self.snake[0]
                # edge case
                if self.size == 3:
                    self.head = self.snake[0]
                    self.snake = [self.head]
                    self.dead = self.head
                self.direction = None
            else:
                self.snake.insert(0, self.head)
            self.update_grid()
            if self.direction_buffer:
                self.direction = self.direction_buffer
                self.direction_buffer = None