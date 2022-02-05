import random


class State:
    def __init__(self, rows = 6, cols = 5):
        self.rows = rows
        self.cols = cols
        self.current_row = 0
        self.current_col = 0
        self.board = [[None for col in range(cols)] for row in range(rows)]
        if self.cols == 4:
            self.words = open('../words/four_letter_words.txt').readlines()
        elif self.cols == 5:
            self.words = open('../words/five_letter_words.txt').readlines()
        else:
            self.words = open('../words/six_letter_words.txt').readlines()
        self.words = [x.strip() for x in self.words]
        self.word = None
        self.guess = None
        self.shake = (-1, 0)
        self.flip = (-1, 0)
        self.guessed_letters = {}
        while not self.word or self.word.endswith('s'):
            self.word = self.words[random.randint(0, 2000)]

    def add_key(self, key):
        if self.current_col < self.cols:
            self.board[self.current_row][self.current_col] = (key.upper(), 'guess')
            self.current_col += 1

    def delete_key(self):
        if self.current_col > 0:
            self.current_col -= 1
            self.board[self.current_row][self.current_col] = None

    def make_guess(self):
        if self.current_col != self.cols:
            return
        guess = ''
        guess_type = [None for i in range(self.cols)]
        for letter_idx in range(self.cols):
            letter = self.board[self.current_row][letter_idx][0]
            guess += letter
        if guess.lower() not in self.words:
            self.shake = (self.current_row, -1)
            return

        word_locs = {}
        for i in range(len(self.word)):
            if self.word[i] not in word_locs:
                word_locs[self.word[i]] = [i]
            else:
                word_locs[self.word[i]].append(i)
        
        for i in range(len(guess)):
            letter = guess[i].lower()
            if letter in word_locs:
                if i in word_locs[letter]:
                    guess_type[i] = 'right'
                    word_locs[letter].remove(i)
                    if word_locs[letter] == []:
                        del word_locs[letter]
        
        for i in range(len(guess)):
            letter = guess[i].lower()
            if not guess_type[i]:
                if letter not in word_locs:
                    guess_type[i] = 'wrong'
                else:
                    guess_type[i] = 'half-right'
                    word_locs[letter].pop()
                    if word_locs[letter] == []:
                        del word_locs[letter]
            self.board[self.current_row][i] = (self.board[self.current_row][i][0], guess_type[i])
        
        for letter, type in zip(guess, guess_type):
            if letter not in self.guessed_letters:
                self.guessed_letters[letter] = type
            else:
                if type == 'right':
                    self.guessed_letters[letter] = type
                elif type == 'half-right' and self.guessed_letters[letter] == 'wrong':
                    self.guessed_letters[letter] = type
        self.guess = guess.lower()
        self.flip = (self.current_row, -1)
        self.current_row += 1
        self.current_col = 0