from random import randint

scores ={"computer": 0, "player": 0}


class board:

    """Board Class"""

    def __init__(self, size, num_ships, names, type):
        self.size = size
        self.board =[["." for x in range(size)] for y in range(size)]
        self.num_ships =num_ships
        self.name = names
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def board_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = '| O'
            return f'{self.name}, you hit and sank a battleship!'
        else:
            return f"{self.name}, you've missed this time..."

    def add_ships(self, x, y, type='computer'):
        if len(self.ships) >= self.ship_nums:
            print('Too many ships')

        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = '| @'


def random_number(size):
    """
    Returns random integer between 0 and the length of the board
    chosen by the player.
    """
    return randint(0, (size) - 1)
        

def valid_coordinates(x, y, board):
     
     """Validating coordinates"""
     try:
         if _x in range(board.size) and _y in range(board.size):
            return True
         else:
            raise ValueError(
                f"Value Must be between 0 and {board.size}")
        except ValueError as _e:
            print(f"Invalid data: {_e}, please try again\n")
        return False


def populate_board(board):
    
    """populating the board"""
    
    print(f"{board.name}'s board:\n")

    size = board.size

    while len(board.ships) != board.ship_nums:
        x = random_number(size)
        y = random_number(size)
        board.add_ships(x, y)

    board.print_board()
    print(board.ships)


def make_guess(board):
    
    """generates random x and y values for computer.player inputs row and col is requested."""
    
    size = board.size

    while True:
        if board.type == 'computer':
            print("Computer's turn to guess")
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            row_guess = input('Enter row num:\n')
            col_guess = input('Enter column num:\n')
            
        row = validate_user_data(str(row_guess), 0, size)
        col = validate_user_data(str(col_guess), 0, size)

        if row and col:
            break

    return [int(row_guess), int(col_guess)]
    
def play_game(computer_board, player_board):
    
    populate_game_board(board)
    print('~' * 60)
    populate_game_board(other_board)
    player_guess = make_guess(board)
    p_row = player_guess[0]
    p_col = player_guess[1]
    validate_guess(board, other_board, p_row, p_col)

    comp_guess = make_guess(other_board)
    c_row = comp_guess[0]
    c_col = comp_guess[1]
    validate_guess(other_board, board, c_row, c_col)

    if len(other_board.guesses) == ships:
            break

print('finished game')

   

def new_game():
    """
    New game. Sets the number of ship and size of the board, resets ther scores and starts the board.
    """


    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 30)
    print(" Welcome to BATTLESHIPS for Dummies!!")
    print(" Board Size: 5. Number of ships: 4")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 30)
    player_name = input("Please enter your name: \n")
    print("-" * 30)


    player_board = Board(size, player_name, "player", num_ships)
    computer_board = Board(size, "computer", "computer", num_ships)

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    
    play_game(player_board, computer_board)

new_game()