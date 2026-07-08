# ~ Movement Functions ~ #


# -- Properly Swap nodes and data -- #
def update_data(grid_data, nodes_data, row, col, row2, col2):
    (
        grid_data[row][col],
        grid_data[row2][col2],
    ) = (
        grid_data[row2][col2],
        grid_data[row][col],
    )
    (nodes_data[row][col].color, nodes_data[row2][col2].color) = (
        nodes_data[row2][col2].color,
        nodes_data[row][col].color,
    )
    (nodes_data[row][col].number, nodes_data[row2][col2].number) = (
        nodes_data[row2][col2].number,
        nodes_data[row][col].number,
    )


# -- Rotating Clockwise -- #
def rotate(grid_data, nodes_data, center, outside=False, outside2=False, back=False):
    normal_offsets = [
        [
            # Swap bottom right with top left
            center[0] + 1,
            center[1] + 1,
            center[0] - 1,
            center[1] - 1,
        ],
        [
            # Swap bottom right with top right
            center[0] + 1,
            center[1] + 1,
            center[0] - 1,
            center[1] + 1,
        ],
        [
            # Swap bottom left with top left
            center[0] + 1,
            center[1] - 1,
            center[0] - 1,
            center[1] - 1,
        ],
        [
            # Swap bottom middle with right middle
            center[0] + 1,
            center[1],
            center[0],
            center[1] + 1,
        ],
        [
            # Swap left middle with top middle
            center[0],
            center[1] - 1,
            center[0] - 1,
            center[1],
        ],
        [
            # Swap right middle with left middle
            center[0],
            center[1] + 1,
            center[0],
            center[1] - 1,
        ],
    ]

    for offset in normal_offsets:
        update_data(grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3])

    if outside and not back:
        # -- Swaps are relative to Middle Square -- #
        outside_offsets = [
            [
                # Swap Top Three with Right Three (Starting at the closest to the top right corner)
                center[0] - 2,
                center[1] + 1,
                center[0] - 1,
                center[1] + 2,
            ],
            [
                center[0] - 2,
                center[1],
                center[0],
                center[1] + 2,
            ],
            [
                center[0] - 2,
                center[1] - 1,
                center[0] + 1,
                center[1] + 2,
            ],
            [
                # Swap Bottom Three with Left Three (Starting at the closest to the bottom left corner)
                center[0] + 2,
                center[1] - 1,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                center[0] + 2,
                center[1],
                center[0],
                center[1] - 2,
            ],
            [
                center[0] + 2,
                center[1] + 1,
                center[0] - 1,
                center[1] - 2,
            ],
            [
                # Swap Top Three with Bottom Three (Starting at the top right corner)
                center[0] - 2,
                center[1] + 1,
                center[0] + 2,
                center[1] + 1,
            ],
            [
                center[0] - 2,
                center[1],
                center[0] + 2,
                center[1],
            ],
            [
                center[0] - 2,
                center[1] - 1,
                center[0] + 2,
                center[1] - 1,
            ],
            [
                # Swap Top of Right with Bottom of Right
                center[0] - 1,
                center[1] + 2,
                center[0] + 1,
                center[1] + 2,
            ],
            [
                # Swap Top of Left with Bottom of Left
                center[0] - 1,
                center[1] - 2,
                center[0] + 1,
                center[1] - 2,
            ],
        ]

        for offset in outside_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )

    if outside and back:
        # -- Swaps are relative to Furthest Right Square -- #
        outside_back_offsets = [
            [
                # Swap Top Three with Right Three (Starting at the closest to the top right corner)
                center[0] - 4,
                center[1] - 7,
                center[0] - 1,
                center[1] - 10,
            ],
            [
                center[0] - 4,
                center[1] - 6,
                center[0],
                center[1] - 10,
            ],
            [
                center[0] - 4,
                center[1] - 5,
                center[0] + 1,
                center[1] - 10,
            ],
            [
                # Swap Bottom Three with Left Three (Starting at the closest to the bottom left corner)
                center[0] + 4,
                center[1] - 5,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                center[0] + 4,
                center[1] - 6,
                center[0],
                center[1] - 2,
            ],
            [
                center[0] + 4,
                center[1] - 7,
                center[0] - 1,
                center[1] - 2,
            ],
            [
                # Swap Top Three with Bottom Three (Starting at the top right corner)
                center[0] - 4,
                center[1] - 7,
                center[0] + 4,
                center[1] - 7,
            ],
            [
                center[0] - 4,
                center[1] - 6,
                center[0] + 4,
                center[1] - 6,
            ],
            [
                center[0] - 4,
                center[1] - 5,
                center[0] + 4,
                center[1] - 5,
            ],
            [
                # Swap Top of Right with Bottom of Right
                center[0] - 1,
                center[1] - 10,
                center[0] + 1,
                center[1] - 10,
            ],
            [
                # Swap Top of Left with Bottom of Left
                center[0] - 1,
                center[1] - 2,
                center[0] + 1,
                center[1] - 2,
            ],
        ]

        for offset in outside_back_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )

    if outside2 and not back:
        outside2_offsets = [
            [
                # Top - Right
                center[0] - 3,
                center[1] + 1,
                center[0] - 1,
                center[1] + 3,
            ],
            [
                center[0] - 3,
                center[1],
                center[0],
                center[1] + 3,
            ],
            [
                center[0] - 3,
                center[1] - 1,
                center[0] + 1,
                center[1] + 3,
            ],
            [
                # Bottom - Left
                center[0] + 3,
                center[1] - 1,
                center[0] + 1,
                center[1] - 3,
            ],
            [
                center[0] + 3,
                center[1],
                center[0],
                center[1] - 3,
            ],
            [
                center[0] + 3,
                center[1] + 1,
                center[0] - 1,
                center[1] - 3,
            ],
            [
                # Swap top and bottom
                center[0] - 3,
                center[1] + 1,
                center[0] + 3,
                center[1] + 1,
            ],
            [
                center[0] - 3,
                center[1],
                center[0] + 3,
                center[1],
            ],
            [
                center[0] - 3,
                center[1] - 1,
                center[0] + 3,
                center[1] - 1,
            ],
            [
                # Swap Top & Bottom from Left side
                center[0] - 1,
                center[1] + 3,
                center[0] + 1,
                center[1] + 3,
            ],
            [
                # Swap Top & Bottom from Right side
                center[0] - 1,
                center[1] - 3,
                center[0] + 1,
                center[1] - 3,
            ],
        ]

        for offset in outside2_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )


# -- Rotating Counter-Clockwise -- #
def counter_rotate(
    grid_data, nodes_data, center, outside=False, outside2=False, back=False
):
    normal_offsets = [
        [
            # Swap bottom left with top right
            center[0] + 1,
            center[1] - 1,
            center[0] - 1,
            center[1] + 1,
        ],
        [
            # Swap bottom left with top left
            center[0] + 1,
            center[1] - 1,
            center[0] - 1,
            center[1] - 1,
        ],
        [
            # Swap bottom right with top right
            center[0] + 1,
            center[1] + 1,
            center[0] - 1,
            center[1] + 1,
        ],
        [
            # Swap bottom middle with left middle
            center[0] + 1,
            center[1],
            center[0],
            center[1] - 1,
        ],
        [
            # Swap right middle with top middle
            center[0],
            center[1] + 1,
            center[0] - 1,
            center[1],
        ],
        [
            # Swap left middle with right middle
            center[0],
            center[1] - 1,
            center[0],
            center[1] + 1,
        ],
    ]

    for offset in normal_offsets:
        update_data(grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3])

    if outside and not back:
        # -- Swaps are relative to Middle Square -- #
        outside_offsets = [
            [
                # Swap Top Three with Left Three (Starting at the closest to the top left corner)
                center[0] - 2,
                center[1] - 1,
                center[0] - 1,
                center[1] - 2,
            ],
            [
                center[0] - 2,
                center[1],
                center[0],
                center[1] - 2,
            ],
            [
                center[0] - 2,
                center[1] + 1,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                # Swap Bottom Three with Right Three (Starting at the closest to the bottom right corner)
                center[0] + 2,
                center[1] + 1,
                center[0] + 1,
                center[1] + 2,
            ],
            [
                center[0] + 2,
                center[1],
                center[0],
                center[1] + 2,
            ],
            [
                center[0] + 2,
                center[1] - 1,
                center[0] - 1,
                center[1] + 2,
            ],
            [
                # Swap Top Three with Bottom Three (Starting at the top left corner)
                center[0] - 2,
                center[1] - 1,
                center[0] + 2,
                center[1] - 1,
            ],
            [
                center[0] - 2,
                center[1],
                center[0] + 2,
                center[1],
            ],
            [
                center[0] - 2,
                center[1] + 1,
                center[0] + 2,
                center[1] + 1,
            ],
            [
                # Swap Top of Left with Bottom of Left
                center[0] - 1,
                center[1] - 2,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                # Swap Top of Right with Bottom of Right
                center[0] - 1,
                center[1] + 2,
                center[0] + 1,
                center[1] + 2,
            ],
        ]

        for offset in outside_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )

    if outside and back:
        # -- Swaps are relative to Furthest Right Square -- #
        outside_back_offsets = [
            [
                # Swap Top Three with Right Three (Starting at the closest to the top right corner)
                center[0] - 4,
                center[1] - 5,
                center[0] - 1,
                center[1] - 2,
            ],
            [
                center[0] - 4,
                center[1] - 6,
                center[0],
                center[1] - 2,
            ],
            [
                center[0] - 4,
                center[1] - 7,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                # Swap Bottom Three with Left Three (Starting at the closest to the bottom left corner)
                center[0] + 4,
                center[1] - 7,
                center[0] + 1,
                center[1] - 10,
            ],
            [
                center[0] + 4,
                center[1] - 6,
                center[0],
                center[1] - 10,
            ],
            [
                center[0] + 4,
                center[1] - 5,
                center[0] - 1,
                center[1] - 10,
            ],
            [
                # Swap Top Three with Bottom Three (Starting at the top right corner)
                center[0] - 4,
                center[1] - 5,
                center[0] + 4,
                center[1] - 5,
            ],
            [
                center[0] - 4,
                center[1] - 7,
                center[0] + 4,
                center[1] - 7,
            ],
            [
                center[0] - 4,
                center[1] - 6,
                center[0] + 4,
                center[1] - 6,
            ],
            [
                # Swap Top of Left with Bottom of Left
                center[0] - 1,
                center[1] - 2,
                center[0] + 1,
                center[1] - 2,
            ],
            [
                # Swap Top of Right with Bottom of Right
                center[0] - 1,
                center[1] - 10,
                center[0] + 1,
                center[1] - 10,
            ],
        ]

        for offset in outside_back_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )

    if outside2 and not back:
        outside2_offsets = [
            [
                # Top - Left
                center[0] - 3,
                center[1] - 1,
                center[0] - 1,
                center[1] - 3,
            ],
            [
                center[0] - 3,
                center[1],
                center[0],
                center[1] - 3,
            ],
            [
                center[0] - 3,
                center[1] + 1,
                center[0] + 1,
                center[1] - 3,
            ],
            [
                # Bottom - RIght
                center[0] + 3,
                center[1] + 1,
                center[0] + 1,
                center[1] + 3,
            ],
            [
                center[0] + 3,
                center[1],
                center[0],
                center[1] + 3,
            ],
            [
                center[0] + 3,
                center[1] - 1,
                center[0] - 1,
                center[1] + 3,
            ],
            [
                # Swap top and bottom
                center[0] - 3,
                center[1] - 1,
                center[0] + 3,
                center[1] - 1,
            ],
            [
                center[0] - 3,
                center[1] + 1,
                center[0] + 3,
                center[1] + 1,
            ],
            [
                center[0] - 3,
                center[1],
                center[0] + 3,
                center[1],
            ],
            [
                # Swap Top & Bottom from Right side
                center[0] - 1,
                center[1] - 3,
                center[0] + 1,
                center[1] - 3,
            ],
            [
                # Swap Top & Bottom from Left side
                center[0] - 1,
                center[1] + 3,
                center[0] + 1,
                center[1] + 3,
            ],
        ]

        for offset in outside2_offsets:
            update_data(
                grid_data, nodes_data, offset[0], offset[1], offset[2], offset[3]
            )


# -- Shift Row to the Left -- #
def shift_left(grid_data, nodes_data, row):
    for _ in range(3):
        carry_out_letter = grid_data[row][0]

        carry_out_node_color = nodes_data[row][0].color
        carry_out_node_number = nodes_data[row][0].number

        for j in range(1, len(grid_data[row])):
            grid_data[row][j - 1] = grid_data[row][j]

            nodes_data[row][j - 1].color = nodes_data[row][j].color
            nodes_data[row][j - 1].number = nodes_data[row][j].number

        grid_data[row][-1] = carry_out_letter

        nodes_data[row][-1].color = carry_out_node_color
        nodes_data[row][-1].number = carry_out_node_number


# -- Shift Row to the Right -- #
def shift_right(grid_data, nodes_data, row):
    for _ in range(3):
        carry_out_letter = grid_data[row][-1]

        carry_out_node_color = nodes_data[row][-1].color
        carry_out_node_number = nodes_data[row][-1].number

        for j in range(len(grid_data[row]) - 2, -1, -1):
            grid_data[row][j + 1] = grid_data[row][j]

            nodes_data[row][j + 1].color = nodes_data[row][j].color
            nodes_data[row][j + 1].number = nodes_data[row][j].number

        grid_data[row][0] = carry_out_letter

        nodes_data[row][0].color = carry_out_node_color
        nodes_data[row][0].number = carry_out_node_number


# -- Shift Col Upwards -- #
def shift_up(grid_data, nodes_data, col):
    for _ in range(3):
        carry_out_letter = grid_data[0][col]

        carry_out_node_color = nodes_data[0][col].color
        carry_out_node_number = nodes_data[0][col].number

        for j in range(1, len(grid_data)):
            grid_data[j - 1][col] = grid_data[j][col]

            nodes_data[j - 1][col].color = nodes_data[j][col].color
            nodes_data[j - 1][col].number = nodes_data[j][col].number

        second_carry_out_letter = grid_data[5][14 - col]
        second_carry_out_node_color = nodes_data[5][14 - col].color
        second_carry_out_node_number = nodes_data[5][14 - col].number

        grid_data[5][14 - col] = grid_data[4][14 - col]
        nodes_data[5][14 - col].color = nodes_data[4][14 - col].color
        nodes_data[5][14 - col].number = nodes_data[4][14 - col].number

        grid_data[4][14 - col] = grid_data[3][14 - col]
        nodes_data[4][14 - col].color = nodes_data[3][14 - col].color
        nodes_data[4][14 - col].number = nodes_data[3][14 - col].number

        grid_data[3][14 - col] = carry_out_letter
        nodes_data[3][14 - col].color = carry_out_node_color
        nodes_data[3][14 - col].number = carry_out_node_number

        grid_data[-1][col] = second_carry_out_letter
        nodes_data[-1][col].color = second_carry_out_node_color
        nodes_data[-1][col].number = second_carry_out_node_number


# -- Shift Col Downwards -- #
def shift_down(grid_data, nodes_data, col):
    for _ in range(3):
        carry_out_letter = grid_data[-1][col]

        carry_out_node_color = nodes_data[-1][col].color
        carry_out_node_number = nodes_data[-1][col].number

        for j in range(len(grid_data) - 2, -1, -1):
            grid_data[j + 1][col] = grid_data[j][col]

            nodes_data[j + 1][col].color = nodes_data[j][col].color
            nodes_data[j + 1][col].number = nodes_data[j][col].number

        second_carry_out_letter = grid_data[3][14 - col]
        second_carry_out_node_color = nodes_data[3][14 - col].color
        second_carry_out_node_number = nodes_data[3][14 - col].number

        grid_data[3][14 - col] = grid_data[4][14 - col]
        nodes_data[3][14 - col].color = nodes_data[4][14 - col].color
        nodes_data[3][14 - col].number = nodes_data[4][14 - col].number

        grid_data[4][14 - col] = grid_data[5][14 - col]
        nodes_data[4][14 - col].color = nodes_data[5][14 - col].color
        nodes_data[4][14 - col].number = nodes_data[5][14 - col].number

        grid_data[5][14 - col] = carry_out_letter
        nodes_data[5][14 - col].color = carry_out_node_color
        nodes_data[5][14 - col].number = carry_out_node_number

        grid_data[0][col] = second_carry_out_letter
        nodes_data[0][col].color = second_carry_out_node_color
        nodes_data[0][col].number = second_carry_out_node_number


### -- Face Turns -- ###


def up(grid_data, nodes_data):
    # -- Shift top of middle row squares to the left (carry out left) -- #
    shift_left(grid_data, nodes_data, 3)

    # -- Rotate Top Square Clockwise -- #
    rotate(grid_data, nodes_data, (1, 4))


def down(grid_data, nodes_data):
    # -- Shift bottom of middle row squares to the right (carry out right) -- #
    shift_right(grid_data, nodes_data, 5)

    # -- Rotate Bottom Square Clockwise -- #
    rotate(grid_data, nodes_data, (7, 4))


def right(grid_data, nodes_data):
    # -- Shift right of middle row squares upwards (carry out top) -- #
    shift_up(grid_data, nodes_data, 5)

    # -- Rotate Square on the right of the Middle Square Clockwise -- #
    rotate(grid_data, nodes_data, (4, 7))


def left(grid_data, nodes_data):
    # -- Shift left of middle row squares downwards (carry out bottom) -- #
    shift_down(grid_data, nodes_data, 3)

    # -- Rotate Square on the left of the Middle Square Clockwise -- #
    rotate(grid_data, nodes_data, (4, 1))


def front(grid_data, nodes_data):
    # -- Rotate Middle Square Clockwise -- #
    rotate(grid_data, nodes_data, (4, 4), True, False, False)


def back(grid_data, nodes_data):
    # -- Rotate furthest Square on the right Clockwise -- #
    rotate(grid_data, nodes_data, (4, 10), True, False, True)


def up_prime(grid_data, nodes_data):
    # -- Shift top of middle row squares to the right (carry out right) -- #
    shift_right(grid_data, nodes_data, 3)

    # -- Rotate Top Square Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (1, 4))


def down_prime(grid_data, nodes_data):
    # -- Shift bottom of middle row squares to the left (carry out left) -- #
    shift_left(grid_data, nodes_data, 5)

    # -- Rotate Bottom Square Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (7, 4))


def right_prime(grid_data, nodes_data):
    # -- Shift right of middle row squares downwards (carry out bottom) -- #
    shift_down(grid_data, nodes_data, 5)

    # -- Rotate Square on the right of the Middle Square Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (4, 7))


def left_prime(grid_data, nodes_data):
    # -- Shift left of middle row squares upwards (carry out top) -- #
    shift_up(grid_data, nodes_data, 3)

    # -- Rotate Square on the left of the Middle Square Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (4, 1))


def front_prime(grid_data, nodes_data):
    # -- Rotate Middle Square Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (4, 4), True, False, False)


def back_prime(grid_data, nodes_data):
    # -- Rotate furthest Square on the right Counter-Clockwise -- #
    counter_rotate(grid_data, nodes_data, (4, 10), True, False, True)


### -- Double Face Turns -- ###


def up_2(grid_data, nodes_data):
    up(grid_data, nodes_data)
    up(grid_data, nodes_data)


def down_2(grid_data, nodes_data):
    down(grid_data, nodes_data)
    down(grid_data, nodes_data)


def right_2(grid_data, nodes_data):
    right(grid_data, nodes_data)
    right(grid_data, nodes_data)


def left_2(grid_data, nodes_data):
    left(grid_data, nodes_data)
    left(grid_data, nodes_data)


def front_2(grid_data, nodes_data):
    front(grid_data, nodes_data)
    front(grid_data, nodes_data)


def back_2(grid_data, nodes_data):
    back(grid_data, nodes_data)
    back(grid_data, nodes_data)


### -- Wide Moves -- ###


# TODO: Add wide moves
def up_wide(grid_data, nodes_data):
    up(grid_data, nodes_data)
    east_prime(grid_data, nodes_data)


def up_wide_prime(grid_data, nodes_data):
    up_prime(grid_data, nodes_data)
    east(grid_data, nodes_data)


def up_wide_2(grid_data, nodes_data):
    up_wide(grid_data, nodes_data)
    up_wide(grid_data, nodes_data)


def down_wide(grid_data, nodes_data):
    down(grid_data, nodes_data)
    east(grid_data, nodes_data)


def down_wide_prime(grid_data, nodes_data):
    down_prime(grid_data, nodes_data)
    east_prime(grid_data, nodes_data)


def down_wide_2(grid_data, nodes_data):
    down_wide(grid_data, nodes_data)
    down_wide(grid_data, nodes_data)


def right_wide(grid_data, nodes_data):
    right(grid_data, nodes_data)
    middle_prime(grid_data, nodes_data)


def right_wide_prime(grid_data, nodes_data):
    right_prime(grid_data, nodes_data)
    middle(grid_data, nodes_data)


def right_wide_2(grid_data, nodes_data):
    right_wide(grid_data, nodes_data)
    right_wide(grid_data, nodes_data)


def left_wide(grid_data, nodes_data):
    left(grid_data, nodes_data)
    middle(grid_data, nodes_data)


def left_wide_prime(grid_data, nodes_data):
    left_prime(grid_data, nodes_data)
    middle_prime(grid_data, nodes_data)


def left_wide_2(grid_data, nodes_data):
    left_wide(grid_data, nodes_data)
    left_wide(grid_data, nodes_data)


def front_wide(grid_data, nodes_data):
    front(grid_data, nodes_data)
    south(grid_data, nodes_data)


def front_wide_prime(grid_data, nodes_data):
    front_prime(grid_data, nodes_data)
    south_prime(grid_data, nodes_data)


def front_wide_2(grid_data, nodes_data):
    front_wide(grid_data, nodes_data)
    front_wide(grid_data, nodes_data)


def back_wide(grid_data, nodes_data):
    back(grid_data, nodes_data)
    south_prime(grid_data, nodes_data)


def back_wide_prime(grid_data, nodes_data):
    back_prime(grid_data, nodes_data)
    south(grid_data, nodes_data)


def back_wide_2(grid_data, nodes_data):
    back_wide(grid_data, nodes_data)
    back_wide(grid_data, nodes_data)


### -- Cube Rotations -- ###


def x(grid_data, nodes_data):
    left_prime(grid_data, nodes_data)
    right_wide(grid_data, nodes_data)


def x_prime(grid_data, nodes_data):
    left(grid_data, nodes_data)
    right_wide_prime(grid_data, nodes_data)


def x_2(grid_data, nodes_data):
    x(grid_data, nodes_data)
    x(grid_data, nodes_data)


def y(grid_data, nodes_data):
    down_prime(grid_data, nodes_data)
    up_wide(grid_data, nodes_data)


def y_prime(grid_data, nodes_data):
    down(grid_data, nodes_data)
    up_wide_prime(grid_data, nodes_data)


def y_2(grid_data, nodes_data):
    y(grid_data, nodes_data)
    y(grid_data, nodes_data)


def z(grid_data, nodes_data):
    front(grid_data, nodes_data)
    south(grid_data, nodes_data)
    back_prime(grid_data, nodes_data)


def z_prime(grid_data, nodes_data):
    front_prime(grid_data, nodes_data)
    south_prime(grid_data, nodes_data)
    back(grid_data, nodes_data)


def z_2(grid_data, nodes_data):
    z(grid_data, nodes_data)
    z(grid_data, nodes_data)


### -- Slice Moves -- ###


def middle(grid_data, nodes_data):
    shift_down(grid_data, nodes_data, 4)


def middle_prime(grid_data, nodes_data):
    shift_up(grid_data, nodes_data, 4)


def middle_2(grid_data, nodes_data):
    middle(grid_data, nodes_data)
    middle(grid_data, nodes_data)


def east(grid_data, nodes_data):
    shift_right(grid_data, nodes_data, 4)


def east_prime(grid_data, nodes_data):
    shift_left(grid_data, nodes_data, 4)


def east_2(grid_data, nodes_data):
    east(grid_data, nodes_data)
    east(grid_data, nodes_data)


def south(grid_data, nodes_data):
    counter_rotate(grid_data, nodes_data, (4, 4))
    rotate(grid_data, nodes_data, (4, 4), False, True, False)


def south_prime(grid_data, nodes_data):
    rotate(grid_data, nodes_data, (4, 4))
    counter_rotate(grid_data, nodes_data, (4, 4), False, True, False)


def south_2(grid_data, nodes_data):
    south(grid_data, nodes_data)
    south(grid_data, nodes_data)
