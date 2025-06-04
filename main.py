from desk import env
import random

all_black_checkers = 12
all_white_checkers = 12

game = True
side = 0
#       функції

#   перетворення входу від гравця на координати

def form_to_move(destination):
    try:
        parts = destination.split()
        result = [ ( int(parts[0]), int(parts[1]) ), ( int(parts[2]), int(parts[3]) ) ]
        return result
    except:
        print("Сталася помилка.")
        return None

def form_env():
    print("\n"*3)
    environment = (f"{env[0][0][0]} | {env[0][1][0]} | {env[0][2][0]} | {env[0][3][0]} | {env[0][4][0]} | {env[0][5][0]} | {env[0][6][0]} | {env[0][7][0]}\n"
                   f"{env[1][0][0]} | {env[1][1][0]} | {env[1][2][0]} | {env[1][3][0]} | {env[1][4][0]} | {env[1][5][0]} | {env[1][6][0]} | {env[1][7][0]}\n"
                   f"{env[2][0][0]} | {env[2][1][0]} | {env[2][2][0]} | {env[2][3][0]} | {env[2][4][0]} | {env[2][5][0]} | {env[2][6][0]} | {env[2][7][0]}\n"
                   f"{env[3][0][0]} | {env[3][1][0]} | {env[3][2][0]} | {env[3][3][0]} | {env[3][4][0]} | {env[3][5][0]} | {env[3][6][0]} | {env[3][7][0]}\n"
                   f"{env[4][0][0]} | {env[4][1][0]} | {env[4][2][0]} | {env[4][3][0]} | {env[4][4][0]} | {env[4][5][0]} | {env[4][6][0]} | {env[4][7][0]}\n"
                   f"{env[5][0][0]} | {env[5][1][0]} | {env[5][2][0]} | {env[5][3][0]} | {env[5][4][0]} | {env[5][5][0]} | {env[5][6][0]} | {env[5][7][0]}\n"
                   f"{env[6][0][0]} | {env[6][1][0]} | {env[6][2][0]} | {env[6][3][0]} | {env[6][4][0]} | {env[6][5][0]} | {env[6][6][0]} | {env[6][7][0]}\n"
                   f"{env[7][0][0]} | {env[7][1][0]} | {env[7][2][0]} | {env[7][3][0]} | {env[7][4][0]} | {env[7][5][0]} | {env[7][6][0]} | {env[7][7][0]}\n")
    print(environment)


#       класи


class squares:
    def __init__(self, cords, available):
        self.available = available
        self.cords = cords

all_squares = []
for i, row in enumerate(env):
    for j, val in enumerate(row):
        if val[0] == "-":
            all_squares.append(squares(available=True, cords=(i, j)))
        else:
            all_squares.append(squares(available=False, cords=(i, j)))

def find_square_tomove(start, dest):
    for square in all_squares:
        if square.cords == start:
            square.available = True

    for square in all_squares:
        if square.cords == dest:
            return square.available
    return False

class checkers:
    def __init__(self, position, color=0):
        self.exists = True
        self.abs_pos = position
        self.promoted = False
        self.mark = "a"
        self.color = color

    def promotion(self):
        if self.promoted == True:
            self.mark = self.mark.upper()
            env[int(self.abs_pos[0])][int(self.abs_pos[1])] = [self.mark]
        

    def move(self, dest_pos):
        if self.exists == True:
            if find_square_tomove(self.abs_pos, dest_pos) == True:
                env[dest_pos[0]][dest_pos[1]] = [self.mark]
                env[self.abs_pos[0]][self.abs_pos[1]] = "-"
                self.abs_pos = dest_pos
            else:
                print("Неможливий хід.")

    def beaten(self):
        self.exists = False
        env[self.abs_pos[0]][self.abs_pos[1]] = ["-"]
        for i in all_squares:
            if i.cords == self.abs_pos:
                i.available = True

class black_checkers(checkers):
    def __init__(self, position):
        super().__init__(position=position)
        self.color = 1
        self.abs_pos = position
        self.mark = "e"

    def promotion(self):
        if int(self.abs_pos[0]) == 7:
            self.promoted = True
        super().promotion()

    def move(self, dest_pos):
        global side
        if self.promoted != True:
            if (int(dest_pos[0]) - int(self.abs_pos[0])) != 1:
                pass
        if ( (dest_pos[0] - self.abs_pos[0]) == (dest_pos[1] - self.abs_pos[1]) ) or ( (dest_pos[0 - self.abs_pos[0]]) == ( self.abs_pos[1] - dest_pos[1] ) ):
            super().move(dest_pos=dest_pos)
            self.promotion()
            side = 0
        else:
            print("Неможливий хід.")
            return

    def beaten(self):
        global all_black_checkers
        all_black_checkers -= 1
        super().beaten()

class white_checkers(checkers):
    def __init__(self, position):
        super().__init__(position=position)
        self.abs_pos = position

    def promotion(self):
        if int(self.abs_pos[0]) == 0:
            self.promoted = True
        super().promotion()

    def move(self, dest_pos):
        global side
        if self.promoted != True:
            if (int(self.abs_pos[0]) - int(dest_pos[0])) != 1:
                print("Неможливий хід.")
                return
        if ( (self.abs_pos[0] - dest_pos[0]) == (self.abs_pos[1] - dest_pos[1])  ) or ( ( self.abs_pos[0] - dest_pos[0]) == (dest_pos[1] - self.abs_pos[1]) ):
            super().move(dest_pos=dest_pos)
            self.promotion()
            side = 1
        else:
            print("Неможливий хід.")
            return

    def beaten(self):
        global all_white_checkers
        all_white_checkers -= 1
        super().beaten()



ally = [white_checkers(position=(5,1)), white_checkers(position=(5,3)), white_checkers(position=(5,5)), white_checkers(position=(5,7)),
        white_checkers(position=(6,0)), white_checkers(position=(6,2)), white_checkers(position=(6,4)), white_checkers(position=(6,6)),
        white_checkers(position=(7,1)), white_checkers(position=(7,3)), white_checkers(position=(7,5)), white_checkers(position=(7,7))]

enemy = [black_checkers(position=(0,0)), black_checkers(position=(0,2)), black_checkers(position=(0,4)), black_checkers(position=(0,6)),
         black_checkers(position=(1,1)), black_checkers(position=(1,3)), black_checkers(position=(1,5)), black_checkers(position=(1,7)),
         black_checkers(position=(2,0)), black_checkers(position=(2,2)), black_checkers(position=(2,4)), black_checkers(position=(2,6))]

# ally[0].promoted = True
# ally[0].promotion()

def find_checker(position): # (5, 1)
    if side == 0:
        for index, value in enumerate(ally):
            if value.abs_pos == position:
                return index
        return None

    else:
        for index, value in enumerate(enemy):
            if value.abs_pos == position:
                return index
        return None

def to_beat():
    for i, ival in enumerate(ally):
        for j, jval in enumerate(enemy):
            for y in all_squares:
                if (((ival.abs_pos[0] - 1), (ival.abs_pos[1] - 1)) == jval.abs_pos and ((jval.abs_pos[0] - 1), (jval.abs_pos[1] - 1) == y.cords) and y.available == True) or (((ival.abs_pos[0] - 1), (ival.abs_pos[1] + 1)) == jval.abs_pos and ((jval.abs_pos[0] - 1), (jval.abs_pos[1] + 1) == y.cords) and y.available == True):
                    enemy[j].beaten()
                    env[ally[i].abs_pos[0]][ally[i].abs_pos[1]] = ["-"]
                    for a in all_squares:
                        if a.cords == ally[i].abs_pos:
                            a.available = True
                            return
                    ally[i].abs_pos = y.cords
                    y.available = False
                    env[ally[i].abs_pos[0]][ally[i].abs_pos[1]] = ["a"]





form_env()

while game:
    try:
        move = form_to_move(input())
        checker = move[0]
        where_to_move = move[1]

        if side == 0:
            ally[find_checker(checker)].move(where_to_move)

        else:
            enemy[find_checker(checker)].move(where_to_move)


        form_env()
    except Exception as exc:
        print(f"Сталася помилка - - > {exc}")