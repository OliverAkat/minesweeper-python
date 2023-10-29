import helpers
import random

class Minesweeper:
    def __init__(self):
        self.flagged_cells = set()
        self.alive = True
        self.dug_squares = set()
        self.board = []
        self.bomb_count = 0
        self.square_count = 0
        self.board_height = 0
        self.board_width = 0
        self.is_first_move = True

    # Initializes the board to default values
    def initialize_board(self):
        self.board_width = helpers.prompt_int("Välj bredden på brädet (1-99): ", 1, 99)
        self.board_height = helpers.prompt_int("Välj höjden på brädet (1-99): ", 1, 99)
        self.square_count = self.board_height*self.board_width
        self.bomb_count = helpers.prompt_int(f"Välj antalet bomber på brädet (1-{self.square_count - 1}): ", 1, self.square_count)


        self.board = [[0]*self.board_width for _ in range(self.board_height)]
        # self.hidden_board = [["*"] * self.board_width for _ in range(self.board_height)] # Replace "w"
        self.dug_squares = set()
        
        self.alive = True
        self.flagged_cells = set()

        self.place_bombs()
        self.assign_values()

    # Welcomes the user to the game
    def intro(self):
        print("""
VÄLKOMMEN TILL
         _______ __                                                          
        |   |   |__|.-----.-----.-----.--.--.--.-----.-----.-----.-----.----.
        |       |  ||     |  -__|__ --|  |  |  |  -__|  -__|  _  |  -__|   _|
        |__|_|__|__||__|__|_____|_____|________|_____|_____|   __|_____|__|  
                                                           |__|              
""")

    def get_random_cell(self):
        return random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)

    # Gets a random empty cell (used to place bombs)
    def get_random_empty_cell(self):
        rand_x, rand_y = self.get_random_cell()

        while self.board[rand_y][rand_x] == -1:
            rand_x, rand_y = self.get_random_cell()

        return rand_x, rand_y

    # returns a board with all the numbers replaced
    def get_hidden_board(self):
        hidden_board = []
        for y in range(self.board_height):
            hidden_row = []
            for x in range(self.board_width):
                if (x, y) in self.dug_squares:
                    hidden_row.append(self.board[y][x])
                elif (x, y) in self.flagged_cells:
                    hidden_row.append('F')
                else:
                    hidden_row.append('*')
            hidden_board.append(hidden_row)

        return hidden_board

    def get_board(self):
        return self.board

    # Diplays the board with added graphics
    def display_board(self, is_hidden):
        board = self.get_hidden_board() if is_hidden else self.get_board()
        start_row = '+------'*self.board_width + '+'

        for n in range(self.board_height):
            print(start_row)
            print('|  ' + '  |  '.join([str(i) if i == -1 else f" {str(i)}" for i in board[n]]) + '  |')

        print(start_row)

    def place_bomb(self):
        rand_x, rand_y = self.get_random_empty_cell()
        self.board[rand_y][rand_x] = -1

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

    # Checks if a given cell is in bounds of the current game-board
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
                is_same_cell = (x, y) == (cell_x, cell_y)
                if self.is_cell_in_bounds(x, y) and is_bomb and not is_same_cell:
                    neighbor_count += 1

        return neighbor_count


    # Digs a cell
    def dig(self, cell_x, cell_y):

        if (cell_x, cell_y) in self.dug_squares:
            return True


        if self.board[cell_y][cell_x] == -1:
            return False

        self.dug_squares.add((cell_x,cell_y)) # tror inte denna ska vara här men funkar inte annars

        if self.board[cell_y][cell_x] > 0:
            return True


        for y in range(cell_y-1, cell_y+2):
            for x in range(cell_x-1, cell_x+2):
                cell_is_dug = (x, y) in self.dug_squares

                if self.is_cell_in_bounds(x, y) and not cell_is_dug:
                    self.dig(x, y)

        return True


    # Toggles the flag for a given cell
    def toggle_flag(self, cell_x, cell_y):
        if (cell_x, cell_y) in self.dug_squares:
            self.dug_squares.remove((cell_x, cell_y))
            return

        self.flagged_cells.add((cell_x, cell_y))


    # Moves a bomb (needed if the first click was on a bomb)
    def move_bomb(self, prev_x, prev_y):
        new_x, new_y = self.get_random_empty_cell()

        self.board[prev_y][prev_x] = 0
        self.board[new_y][new_x] = -1

        self.assign_values()

    # Endgame screen for wins
    def win_screen(self):
        print('Grattis på födelsedagen du vann!!!!!!!')

    # Endgame screen for losses
    def loss_screen(self):
        print('Ajdå jobbigt läge brush du torskade :(')

    # Handles the endgame
    def handle_endgame(self, has_won):
        if has_won:
            self.win_screen()
        else:
            self.loss_screen()

        self.alive = False

    # Contains the main game loop
    def play(self):
        self.intro()
        self.initialize_board()
        while self.alive:
            self.display_board(True)

            choice_x = helpers.prompt_int('x: ', 0, self.board_width-1)
            choice_y = helpers.prompt_int('y: ', 0, self.board_height-1)

            choice = input("dig or flag? d/F: ")

            if choice == "d":
                if self.is_first_move and self.board[choice_y][choice_x] == -1:
                    self.move_bomb(choice_x, choice_y)

                is_safe_cell = self.dig(choice_x, choice_y)
                self.is_first_move = False
                if not is_safe_cell:
                        self.handle_endgame(False)
            else:
                self.toggle_flag(choice_x, choice_y)

            if len(self.dug_squares) == (self.square_count - self.bomb_count):
                self.handle_endgame(True)

        self.display_board(False)


Minesweeper().play()


    
     












