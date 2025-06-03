from desk import env
print(f"\n\n\n")
#       функції

environment = str()
def form_env():
    global environment
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

def find_square(start, dest):
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
        

    def move(self, dest_pos):
        if find_square(self.abs_pos, dest_pos) == True:
            env[dest_pos[0]][dest_pos[1]] = [self.mark]
            env[self.abs_pos[0]][self.abs_pos[1]] = "-"
            self.abs_pos = dest_pos
        else:
            print("Неможливий хід.")
        form_env()

class black_checkers(checkers):
    def __init__(self, position):
        super().__init__(position=position)
        self.color = 1
        self.abs_pos = position
        self.mark = "e"

    def move(self, dest_pos):
        super().move(dest_pos=dest_pos)

class white_checkers(checkers):
    def __init__(self, position):
        super().__init__(position=position)
        self.position = position

    def move(self, dest_pos):
        super().move(dest_pos=dest_pos)



form_env()

white_checkers(position=(5,1)).move((4, 0))
white_checkers(position=(4, 0)).move((3, 1))
