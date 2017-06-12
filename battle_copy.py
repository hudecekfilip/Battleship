import copy
import string
from player import Player

MISS = '.'
HIT = '*'
SUNK = '#'


class Battle(Player):
    all_sunked = False
    winner = None


    def setup(self):
        player1 = Battle()
        player2 = Battle()
        player1.shipyard()
        self.clear_screen()
        player2.shipyard()


        (self.empty_board, self.hitted_ships, self.missed_ships,
        self.sunked_ships, self.player_ship_copy, self.player_ship_copy_2) = player1.ahojky(
        player_ship = self.correct_ships_all[1])
        (self.empty_board, self.hitted_ships, self.missed_ships,
        self.sunked_ships, self.player_ship_copy, self.player_ship_copy_2) = player2.ahojky(
        player_ship = self.correct_ships_all[0])

        while not self.all_sunked:
            if not self.all_sunked:
                (self.hitted_ships, self.missed_ships,
                self.all_sunked, self.winner) = player1.attack(
                self.empty_board, self.all_sunked, self.winner, self.hitted_ships,
                self.missed_ships, self.player_ship_copy, self.player_ship_copy_2)
            if not self.all_sunked:
                (self.hitted_ships, self.missed_ships,
                self.all_sunked, self.winner) = player2.attack(
                self.empty_board, self.all_sunked, self.winner, self.hitted_ships,
                self.missed_ships, self.player_ship_copy, self.player_ship_copy_2)
            else:
                pass
        print("Winner is: {}".format(self.winner))


    def ahojky(self, player_ship):
        self.empty_board = self.buildboard()
        self.player_ship_copy = copy.deepcopy(player_ship)
        self.player_ship_copy_2 = copy.deepcopy(player_ship)
        self.hitted_ships = []
        self.sunked_ships = []
        self.missed_ships = []
        return (self.empty_board, self.hitted_ships, self.missed_ships,
                self.sunked_ships, self.player_ship_copy, self.player_ship_copy_2)


    def attack(self, all_sunked, winner, hitted_ships, missed_ships, empty_board,
               player_ship_copy, player_ship_copy_2):
        self.clear_screen()
        ok = False
        while not ok:
            attack_ship_location_x = self.attack_place_a_ship_x()
            attack_ship_location_y = self.attack_place_a_ship_y()
            attack_loc_2, converted_letter, ok = self.attack_check(ok)
        hitted, ship_length = self.miss_or_hit(player_ship_copy, attack_loc_2, converted_letter)
        self.missed_ships, self.player_ship_copy = self.position_remover(hitted,
        player_ship_copy, ship_length, attack_loc_2)
        sunked, hitted, self.player_ship_copy = self.is_sunk(hitted, ship_length,
        player_ship_copy, player_ship_copy_2)
        self.all_sunked, self.player_ship_copy, self.winner = self.testicek(player_ship_copy, winner)
        self.add_value_to_the_board(hitted, empty_board, sunked)
        return self.hitted_ships, self.missed_ships, self.all_sunked, self.winner


    def attack_place_a_ship_x(self):
        # prompt y location a validate user input
        self.attack_loc = []
        print("{}, where do you want to shoot? :".format(self.name))
        attack_ship_location_x = input(
        "Place the 'x' location of the shoot (A-J) ").lower()
        if len(attack_ship_location_x) < 2 and attack_ship_location_x in "abcdefghij":
            self.attack_loc.append(attack_ship_location_x[:])
        else:
            print("You entered a wrong value. Location must be between letters A-J")
            self.attack_place_a_ship_x()
        return self.attack_loc


    def attack_place_a_ship_y(self):
        # promp y location a validate user input
        try:
            attack_ship_location_y = int(
            input("Place the 'y' location of the shoot (1-10) "))
        except ValueError:
            print("You have to enter a number!")
            return self.attack_place_a_ship_y()
        else:
            if attack_ship_location_y <= 10:
                self.attack_loc.append(attack_ship_location_y)
            else:
                print("You entered a wrong value. Number must be between 1-10!")
                return self.attack_place_a_ship_y()
        return self.attack_loc


    def attack_check(self, ok):
        # checks if you are not attacking on the same place
        self.attack_loc_2 = []
        self.missed_ships_a = []
        self.hitted_ships_a = []
        self.sunked_ships_a = []
        converted_letter = string.ascii_lowercase.index(self.attack_loc[0])
        self.attack_loc_2.append((self.attack_loc[1] - 1, converted_letter))

        for x in self.missed_ships:
            for y in x:
                self.missed_ships_a.append(y)

        for x in self.hitted_ships:
            for y in x:
                self.hitted_ships_a.append(y)

        for x in self.sunked_ships:
            for y in x:
                self.sunked_ships_a.append(y)

        for val in self.attack_loc_2:
            if val in self.hitted_ships_a:
                print("You have already shoot on this position\n"
                        "Shoot again please!")
            elif val in self.missed_ships_a:
                print("You have already shoot on this position\n"
                        "Shoot again please!")
            elif val in self.sunked_ships_a:
                print("You have already shoot on this position\n"
                        "Shoot again please!")
            else:
                ok = True
        return self.attack_loc_2, converted_letter, ok


    def miss_or_hit(self, player_ship_copy, attack_loc_2, converted_letter):
        # checks if you hit an opponent ship or not
        hitted = False
        count10 = 0
        self.player_ship_copy = [x for x in self.player_ship_copy if x != []]
        self.ship_length = len(self.player_ship_copy)
        while count10 < self.ship_length:
            for val in self.attack_loc_2:
                if val in self.player_ship_copy[count10][1]:
                    hitted = True
                    self.hitted_ships.append(self.attack_loc_2[:])
                    print("Well Done! You hitted part of {}"
                    .format(self.player_ship_copy[count10][0]))
                else:
                    pass
            count10 += 1
        return hitted, self.ship_length


    def position_remover(self, hitted, player_ship_copy, ship_length, attack_loc_2):
        # remove hitted boats from correct_ships_all list
        if hitted:
            count = 0
            while count < self.ship_length:
                a = [x for x in self.player_ship_copy[count][1] if x not in self.attack_loc_2]
                self.player_ship_copy[count][1] = a
                count += 1
        else:
            print("You missed!")
            self.missed_ships.append(self.attack_loc_2[:])
        return self.missed_ships, self.player_ship_copy


    def is_sunk(self, hitted, ship_length, player_ship_copy, player_ship_copy_2):
        # vytvorit fci, která kontroluje, jestli je lod potopena
        count = 0
        sunked = False
        while count < self.ship_length:
            count += 1
            if not self.player_ship_copy[count - 1][1]:
                sunked = True
                hitted = False
                self.player_ship_copy[count - 1].clear()
                self.player_ship_copy = [x for x in self.player_ship_copy if x != []]
                self.sunked_ships.append(self.player_ship_copy_2[count - 1][1])
                self.player_ship_copy = [x for x in self.player_ship_copy if x != []]
                break
            else:
                pass
        return sunked, hitted, self.player_ship_copy


    def testicek(self, player_ship_copy, winner):
        # fce, která kontroluje jestli je player_ship_copy prazdne
        # to znamena, ze hrac vyhral
        if self.player_ship_copy:
            pass
        else:
            self.winner = self.name
            self.all_sunked = True
        return self.all_sunked, self.player_ship_copy, self.winner


    def add_value_to_the_board(self, hitted, empty_board, sunked):
        ab = []
        for x in self.attack_loc_2[0]:
            ab.append(x)
        a = ab[0]
        b = ab[1]
        if hitted:
            self.empty_board[a][b] = HIT
        elif sunked:
            cd = []
            for x in self.sunked_ships:
                for y in x:
                    cd.append(y)
            length = len(cd)
            count = 0
            while count < length:
                count += 1
                c = cd[count - 1][0]
                d = cd[count - 1][1]
                self.empty_board[c][d] = SUNK
        else:
            self.empty_board[a][b] = MISS

        print("OPPONENT'S BOARD:")
        self.print_board(self.empty_board)

if __name__ == "__main__":
    foo = Battle()
    foo.setup()
