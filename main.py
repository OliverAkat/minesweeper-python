import helpers
import random

class Minesweeper:
    def __init__(self):
        self.initialize_board()

    # Initializes the board to default values
    def initialize_board(self):
        self.board_width = helpers.prompt_int("Välj bredden på brädet (1-99): ", 1, 99)
        self.board_height = helpers.prompt_int("Välj höjden på brädet (1-99): ", 1, 99)
        self.square_count = self.board_height*self.board_width
        self.bomb_count = helpers.prompt_int(f"Välj antalet bomber på brädet (1-{self.square_count - 1}): ", 1, self.square_count)


        self.board = [[0]*self.board_width for _ in range(self.board_height)]
        self.dug_squares = set()
        self.alive = True
        self.flagged_cells = set()

        self.place_bombs()
        self.assign_values()

    # Welcomes the user to the game
    def intro(self):
        pass

    def get_random_cell(self):
        return random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)

    # Gets a random empty cell (used to place bombs)
    def get_random_empty_cell(self):
        rand_x, rand_y = self.get_random_cell()

        while self.board[rand_y][rand_x] == -1:
            rand_x, rand_y = self.get_random_cell()

        return rand_x, rand_y


    # diplays the board with added graphics
    def display_board(self, board):
        
        start_row = '+------'*self.board_width + '+'

        for n in range(self.board_height):
            print(start_row)
            print('|  ' + '  |  '.join([str(i) if i == -1 else f" {str(i)}" for i in board[n]]) + '  |')

        print(start_row)

    def place_bomb(self):
        rand_x, rand_y = self.get_random_empty_cell()
        self.board[rand_y][rand_x] = -1
        #self.dug_squares.add((rand_y, rand_x))

    # Places all the bombs on the board
    def place_bombs(self):
        for _ in range(self.bomb_count):
            self.place_bomb()

    # Assigns the value to all opened cells
    def assign_values(self):
        for row in range(self.board_height):
            for col in range(self.board_width):
                if self.board[row][col] == -1:
                    continue

                self.board[row][col] = self.count_neighbouring_bombs(col, row)


    # Gets the value of a cell
    def get_cell_value(self, cell_x, cell_y):
        return self.board[cell_y][cell_x]

    def is_cell_in_bounds(self, cell_x, cell_y):
        return 0 <= cell_x < self.board_width and 0 <= cell_y < self.board_height

    # Counts the amount of neighbouring bombs to a cell
    def count_neighbouring_bombs(self, cell_x, cell_y):
        neighbor_count = 0
        for y in range(cell_y-1, cell_y+2):
            for x in range(cell_x-1, cell_x+2):
                if not self.is_cell_in_bounds(x, y):
                    continue

                is_bomb = self.board[y][x] == -1
                is_same_cell = (y, x) == (cell_y, cell_x)
                if self.is_cell_in_bounds(x, y) and is_bomb and not is_same_cell:
                    neighbor_count += 1

        return neighbor_count


    # Digs a cell
    def dig(self, cell_x, cell_y):
        if (cell_x, cell_y) in self.dug_squares:
            return

        if self.board[cell_y][cell_x] == -1:
            return False

        if self.board[cell_y][cell_x] > 0:
            self.dug_squares.add((cell_x,cell_y)) 
            return True

        for x in range(cell_x-1, cell_x+2):
            for y in range(cell_y-1, cell_y+2):
                is_same_cell = (x, y) == cell_x, cell_y
                cell_is_dug = (x, y) in self.dug_squares

                if self.is_cell_in_bounds(x, y) and not is_same_cell and not cell_is_dug:
                    self.dig(x, y)

        return True


    # Toggles the flag for a given cell
    def toggle_flag(self, cell_x, cell_y):
        if (cell_x, cell_y) in self.dug_squares:
            self.dug_squares.remove((cell_x, cell_y))
            return

        self.dug_squares.add((cell_x, cell_y))

    # Moves a bomb (needed if the first click was on a bomb)
    def move_bomb(self, cell_x, cell_y):
        self.board[cell_y][cell_x] = 0

        new_x, new_y = self.get_random_empty_cell()

        # Make sure we don't place the bomb on the same place as before
        while (new_x, new_y) == (cell_x, cell_y):
            new_x, new_y = self.get_random_empty_cell()

        self.board[cell_y][cell_x] = -1
        self.assign_values()


    # returns a board with all the numbers replaced
    def hide_board(self):
        hiddenboard = [["w"]*self.board_width for _ in range(self.board_height)]

        for (x,y) in self.dug_squares:
            hiddenboard[x][y] = "q"

        return hiddenboard

    def get_board(self):
        return self.board

    # Endgame screen for wins
    def win_screen(self):
        print('Grattis på födelsedagen du vann!!!!!!!')
        pass

    # Endgame screen for losses
    def loss_screen(self):
        print('Ajdå jobbigt läge brush du torskade :(')

    # Handles the endgame
    def handle_endgame(self):
        pass

game = Minesweeper()


print(game.dug_squares)
game.display_board(game.hide_board())
game.display_board(game.get_board())








