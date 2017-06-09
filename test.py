correct_ships_all = [
[
['Aircraft Carrier', [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]],
['Battleship', [(0, 1), (1, 1), (2, 1), (3, 1)]],
['Submarine', [(0, 2), (1, 2), (2, 2)]],
['Cruiser', [(0, 3), (1, 3), (2, 3)]],
['Patrol Boat', [(0, 4), (1, 4)]]
],
[
['Aircraft Carrier', [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]],
['Battleship', [(1, 0), (1, 1), (1, 2), (1, 3)]],
['Submarine', [(2, 0), (2, 1), (2, 2)]],
['Cruiser', [(3, 0), (3, 1), (3, 2)]],
['Patrol Boat', [(4, 0), (4, 1)]]
]
]

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
BOARD_SIZE = 10
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = "#"
empty_board = [
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ]


tralala = [['O', '|', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', '|', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]


sunked_ships = [[(0, 3)], [(0, 2), (1, 2)], [(1, 2), (2, 2), (3, 4)]]


def buildboard():
    """Creates empty board according to BOARD_SIZE & EMPTY"""
    board = [[EMPTY] * BOARD_SIZE for cell in range(BOARD_SIZE)]
    return board


def print_board(board):
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1

print_board(tralala)
