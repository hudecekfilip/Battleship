import copy
import string
from boardbuilder import BoardBilder

SHIP_INFO = [
    ("Aircraft Carrier", 2),
    #("Battleship", 1),
    #("Submarine", 3),
    #("Cruiser", 3),
    #("Patrol Boat", 2)
]

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
BOARD_SIZE = 10
EMPTY = 'O'

class Player(BoardBilder):
    # all correct placed ships, player 1 = correct_ships_all[0],
    # player2 = correct_ships_all[1]
    correct_ships_all = []
    final_board = []
    empty_board = []


    def shipyard(self):
        board = self.buildboard()
        self.insert_name()
        self.ship = []
        self.ships = []
        self.ships_all = []
        self.correct_ships = []
        count = 0
        for each in SHIP_INFO:
            count += 1
            go_on = False
            while not go_on:
                self.ship_location_x = self.place_a_ship_x(each)
                self.ship_location_y = self.place_a_ship_y(each)
                vertical = self.vert_or_hor()
                self.ship_builder(each, vertical)
                go_on = self.boarder_checker(each, vertical, go_on)
                self.cosi(each, go_on)
                self.add_ships_to_the_board(vertical, each, go_on, count)
            self.print_board(self.board)
        self.final_board.append(self.board)
        self.correct_ships_all.append(self.correct_ships)
        self.ships_all.clear()
        return self.correct_ships


    def insert_name(self):
        print("Hello, welcome to BattleShip Game\n"
                "Let`s get started!")
        self.name = input("What`s your name?:\n")
        return self.name


    def place_a_ship_x(self, each):
        self.ship_location_x = input("Place the 'x' location of the {}: (A-J) "
        .format(each[0])).lower()
        if len(self.ship_location_x) < 2 and self.ship_location_x in "abcdefghij":
            self.ship.append(self.ship_location_x[:])
        else:
            print("You entered a wrong value. Location must be between letters A-J")
            self.place_a_ship_x(each)
        return self.ship


    def place_a_ship_y(self, each):
        try:
            self.ship_location_y = int(input("Place the 'y' location of the {}: (1-10) "
            .format(each[0])))
        except ValueError:
            print("You have to enter a number!")
            return self.place_a_ship_y(each)
        else:
            if self.ship_location_y <= 10:
                self.ship.append(self.ship_location_y)
            else:
                print("You entered a wrong value. Number must be between 1-10!")
                return self.place_a_ship_y(each)
        return self.ship


    def vert_or_hor(self):
        self.v_or_h = input("Vertical or Horizontal?:(V/H) ").lower()
        vertical = True
        if self.v_or_h == "v":
            return vertical
        elif self.v_or_h == "h":
            vertical = False
            return vertical
        else:
            print("Entered value must me 'v' or 'h'!")
            self.vert_or_hor()


    def ship_builder(self, each, vertical):
        self.converted_letter = string.ascii_lowercase.index(self.ship[0])
        self.count4 = 0
        if vertical:
            for x in range(each[1]):
                self.ships.append((self.ship[1] - 1 + self.count4,
                self.converted_letter))
                self.count4 += 1
        else:
            for y in range(each[1]):
                self.ships.append((self.ship[1] - 1,
                self.converted_letter + self.count4))
                self.count4 += 1
        return self.ships


    def boarder_checker(self, each, vertical, go_on):
        self.converted_letter = string.ascii_lowercase.index(self.ship[0])
        self.problem_solver = BOARD_SIZE - each[1] + 1
        if vertical:
            if self.ship[1] > each[1]:
                print("Your ship {} is partly outside of the field".format(each[0]))
                print("Please insert the coordinates again!")
                go_on = False
                return go_on
            elif [item for item in self.ships if item in self.ships_all]:
                print("Another ship is in the way!")
                print("Please insert the coordinates again!")
                go_on = False
                return go_on
            else:
                go_on = True
                return go_on
        else:
            print("self.problem_solver:")
            print(self.problem_solver)
            print("converted_letter: {}".format(self.converted_letter))
            if self.converted_letter >= self.problem_solver:
                print("Your ship {} is partly outside of the field".format(each[0]))
                print("Please insert the coordinates again!")
                go_on = False
                return go_on
            elif [item for item in self.ships if item in self.ships_all]:
                print("Another ship is in the way!")
                print("Please insert the coordinates again!")
                go_on = False
                return go_on
            else:
                go_on = True
                return go_on


    def cosi(self, each, go_on):
        if go_on:
            for x in self.ships:
                self.ships_all.append(x[:])
            self.correct_ships.append([each[0], self.ships[:]])
            self.ships.clear()
            self.ship.clear()
            return self.ships_all, self.correct_ships
        else:
            self.ship.clear()
            self.ships.clear()


    def add_ships_to_the_board(self, vertical, each, go_on, count):
        self.length = SHIP_INFO[count-1][1]
        if go_on:
            if vertical:
                self.list2 = []
                self.count2 = 0
                while self.count2 < self.length:
                    for x in self.correct_ships[count-1][1][self.count2]:
                        self.list2.append(x)
                    self.count2 += 1
                    self.a = self.list2[0]
                    self.b = self.list2[1]
                    self.board[self.a][self.b] = VERTICAL_SHIP
                    self.list2.clear()
                return self.board
            else:
                self.list3 = []
                self.count3 = 0
                while self.count3 < self.length:
                    for y in self.correct_ships[count-1][1][self.count3]:
                        self.list3.append(y)
                    self.count3 += 1
                    self.c = self.list3[0]
                    self.d = self.list3[1]
                    self.board[self.c][self.d] = HORIZONTAL_SHIP
                    self.list3.clear()
                return self.board
        else:
            pass
