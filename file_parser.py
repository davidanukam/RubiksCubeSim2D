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
    # Wide Moves (Lower case notation)
    "u": up_wide,
    "u'": up_wide_prime,
    "u2": up_wide_2,
    "d": down_wide,
    "d'": down_wide_prime,
    "d2": down_wide_2,
    "r": right_wide,
    "r'": right_wide_prime,
    "r2": right_wide_2,
    "l": left_wide,
    "l'": left_wide_prime,
    "l2": left_wide_2,
    "f": front_wide,
    "f'": front_wide_prime,
    "f2": front_wide_2,
    "b": back_wide,
    "b'": back_wide_prime,
    "b2": back_wide_2,
    # Wide Moves (w notation)
    "Uw": up_wide,
    "Uw'": up_wide_prime,
    "Uw2": up_wide_2,
    "Dw": down_wide,
    "Dw'": down_wide_prime,
    "Dw2": down_wide_2,
    "Rw": right_wide,
    "Rw'": right_wide_prime,
    "Rw2": right_wide_2,
    "Lw": left_wide,
    "Lw'": left_wide_prime,
    "Lw2": left_wide_2,
    "Fw": front_wide,
    "Fw'": front_wide_prime,
    "Fw2": front_wide_2,
    "Bw": back_wide,
    "Bw'": back_wide_prime,
    "Bw2": back_wide_2,
    # Rotations
    "x": x,
    "x'": x_prime,
    "x2": x_2,
    "y": y,
    "y'": y_prime,
    "y2": y_2,
    "z": z,
    "z'": z_prime,
    "z2": z_2,
    # Slice Moves
    "M": middle,
    "M'": middle_prime,
    "M2": middle_2,
    "E": east,
    "E'": east_prime,
    "E2": east_2,
    "S": south,
    "S'": south_prime,
    "S2": south_2,
}


def get_moves_from_file(file_name):
    moves = []

    try:
        with open(file_name, "r") as f:
            content = f.read()
            raw_moves = content.split()

            for m in raw_moves:
                mapped_move = move_map.get(m)

                if mapped_move is not None:
                    moves.append(mapped_move)
                else:
                    print(f"Warning: Move '{m}' not found in move_map.")

    except Exception as e:
        print(f"Error reading file: {e}")

    return moves
