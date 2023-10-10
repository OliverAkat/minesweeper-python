class Minesweeper:
    def __init__(self):
        pass

    # Initializes the board to default values
    def initialize_board(self):
        pass

    # Welcomes the user to the game
    def intro(self):
        pass

    # Gets a random empty cell (used to place bombs)
    def get_random_empty_cell(self):
        pass

    # Places a bomb on an empty cell
    def place_bombs(self):
        pass

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
