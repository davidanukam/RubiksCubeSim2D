from movement import *

move_map = {
    "U": up,
    "U'": up_prime,
    "U2": up_2,
    "D": down,
    "D'": down_prime,
    "D2": down_2,
    "R": right,
    "R'": right_prime,
    "R2": right_2,
    "L": left,
    "L'": left_prime,
    "L2": left_2,
    "F": front,
    "F'": front_prime,
    "F2": front_2,
    "B": back,
    "B'": back_prime,
    "B2": back_2,
}


def get_moves_from_file(file_name):
    moves = []

    try:
        with open(file_name, "r") as f:
            line = f.readline()
            move = ""
            for info in line:
                if info != " ":
                    move += info
                else:
                    moves.append(move_map.get(move))
                    move = ""
    except Exception as e:
        print("\n", e)

    return moves
