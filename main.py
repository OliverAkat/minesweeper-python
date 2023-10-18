import helpers
import random

class Minesweeper:
    def __init__(self):
        self.initialize_board()

    # Initializes the board to default values
    def initialize_board(self):
        # Dessa gav errors så behövde kommentera bort just nu
        #self.board_width = helpers.prompt_int("Välj bredden på brädet (1-99): ", 1, 99)
        #self.board_height = helpers.prompt_int("Välj höjden på brädet (1-99): ", 1, 99)
        #self.square_count = self.board_height*self.board_width
        #self.bomb_count = helpers.prompt_int(f"Välj antalet bomber på brädet (1-{self.square_count - 1}): ", 1, self.square_count)
       

        # Här har jag bara manuelt lagt in värden
        self.board_width = 10
        self.board_height = 10
        self.square_count = self.board_width*self.board_height
        self.bomb_count = 95


        self.board = [[0]*self.board_width for _ in range(self.board_height)]
        self.dug_squares = set()
        self.alive = True
        self.flagged_cells = set()

        self.place_bombs()
        self.assign_values()

    # Welcomes the user to the game
    def intro(self):
        pass

    # Gets a random empty cell (used to place bombs)
    def get_random_empty_cell(self):
        return (random.randint(0, self.board_width-1),random.randint(0,self.board_height-1))

    def display_board(self): 
        for n in range(self.board_height):
            print(self.board[n])

    # Places a bomb on an empty cell
    def place_bombs(self):
        #n1 = get_random_empty_cell(self)
        i = 0
        while i < self.bomb_count:
            rand_position = self.get_random_empty_cell()
            #print(i, self.bomb_count)
            if self.board[rand_position[1]][rand_position[0]] == 1:
                continue
            
            self.board[rand_position[1]][rand_position[0]] = 1
            print(rand_position)
            i+=1


        #for i in range(self.bomb_count):

            

    # Assigns the value to all opened cells
    def assign_values(self):
        pass

    # Gets the value of a cell
    def get_cell_value(self, cell_index):
        pass

    # Counts the amount of neighbouring bombs to a cell
    def count_neighbouring_bombs(self, cell_index):
        pass

    # Digs a cell
    def dig(self, cell_index):
        pass

    # Toggles the flag for a given cell
    def toggle_flag(self, cell_index):
        pass

    # Moves a bomb (needed if the first click was on a bomb)
    def move_bomb(self, cell_index):
        pass

    # Endgame screen for wins
    def win_screen(self):
        pass

    # Endgame screen for losses
    def loss_screen(self):
        pass

    # Handles the endgame
    def handle_endgame(self):
        pass

game = Minesweeper()


game.display_board()
game.place_bombs()
#print(game.get_random_empty_cell())

