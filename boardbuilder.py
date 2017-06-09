BOARD_SIZE = 10
EMPTY = 'O'


class BoardBilder:
    def buildboard(self):
        """Creates empty board according to BOARD_SIZE & EMPTY"""
        self.board = [[EMPTY] * BOARD_SIZE for cell in range(BOARD_SIZE)]
        return self.board


    def clear_screen(self):
        print("Your opponent is on turn")
        input("Press any key to clear the screen")
        print("\033c", end="")


    def print_board(self, board):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
