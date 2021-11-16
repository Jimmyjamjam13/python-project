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



def make_guess(board):



def play_game(computer_board, player_board):



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