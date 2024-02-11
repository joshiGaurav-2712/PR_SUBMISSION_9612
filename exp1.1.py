import random

# Initialize the board
board = [' ' for _ in range(9)]

def main():
    print('Welcome to Tic-Tac-Toe using Brute Force Technique!\n')
    print_board()

    game_end = False

    while not game_end:
        # Player's turn
        print('\nPlayer\'s turn')
        player_turn()
        print_board()

        if check_winner(board, 'X'):
            print('\nPlayer won!')
            game_end = True
            break

        if board.count(' ') == 0:
            print('\nTie game!')
            game_end = True
            break

        # Computer's turn
        print('\nComputer\'s turn')
        computer_move()
        print_board()

        if check_winner(board, 'O'):
            print('\nComputer won!')
            game_end = True
            break

        if board.count(' ') == 0:
            print('\nTie game!')
            game_end = True
            break

    print('\nGame ended')

def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def player_turn():
    while True:
        try:
            position = int(input('Enter your move (1-9): '))
            if 1 <= position <= 9 and board[position - 1] == ' ':
                board[position - 1] = 'X'
                break
            else:
                print('Invalid move! Try again.')
        except ValueError:
            print('Invalid input! Please enter a number.')

def computer_move():
    available_moves = [i for i, val in enumerate(board) if val == ' ']

    # Look for winning move or blocking move
    for player in ['O', 'X']:
        for move in available_moves:
            board_copy = board[:]
            board_copy[move] = player
            if check_winner(board_copy, player):
                board[move] = 'O'
                return

    # Choose a random move
    random_move = random.choice(available_moves)
    board[random_move] = 'O'

if __name__ == '__main__':
    main()


# Welcome to Tic-Tac-Toe using Brute Force Technique!

#   |   |  
# ---------
#   |   |  
# ---------
#   |   |  

# Player's turn
# Enter your move (1-9): 1
# X |   |  
# ---------
#   |   |  
# ---------
#   |   |  

# Computer's turn
# X |   | O
# ---------
#   |   |
# ---------
#   |   |

# Player's turn
# Enter your move (1-9): 2
# X | X | O
# ---------
#   |   |
# ---------
#   |   |

# Computer's turn
# X | X | O
# ---------
#   |   |
# ---------
#   | O |

# Player's turn
# Enter your move (1-9): 6
# X | X | O
# ---------
#   |   | X
# ---------
#   | O |

# Computer's turn
# X | X | O
# ---------
# O |   | X
# ---------
#   | O |

# Player's turn
# Enter your move (1-9): 5
# X | X | O
# ---------
# O | X | X
# ---------
#   | O |

# Computer's turn
# X | X | O
# ---------
# O | X | X
# ---------
#   | O | O

# Player's turn
# Enter your move (1-9): 7
# X | X | O
# ---------
# O | X | X
# ---------
# X | O | O

# Tie game!
    
# Welcome to Tic-Tac-Toe using Brute Force Technique!

#   |   |  
# ---------
#   |   |  
# ---------
#   |   |  

# Player's turn
# Enter your move (1-9): 2
#   | X |  
# ---------
#   |   |  
# ---------
#   |   |  

# Computer's turn
#   | X |
# ---------
#   | O |
# ---------
#   |   |

# Player's turn
# Enter your move (1-9): 3
#   | X | X
# ---------
#   | O |
# ---------
#   |   |

# Computer's turn
# O | X | X
# ---------
#   | O |
# ---------
#   |   |

# Player's turn
# Enter your move (1-9): 4
# O | X | X
# ---------
# X | O |
# ---------
#   |   |

# Computer's turn
# O | X | X
# ---------
# X | O |
# ---------
#   |   | O

# Computer won!