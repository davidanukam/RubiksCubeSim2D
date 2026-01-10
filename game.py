import contextlib

with contextlib.redirect_stdout(None):
    import pygame

import sys, pywinstyles, random
from colors import *
from movement import *
from node import Node
from solve_button import SolveButton
from cube_data import cube_grid
from file_parser import get_moves_from_file


def game():
    global count

    # -- Exit if too many arguments are passed -- #
    if len(sys.argv) > 2:
        print("\n***** ERROR: Too many arguments! *****")
        print("\nUsage: python main.py [<file_name>]")
        return

    # --  Node Variables -- #
    node_width, node_height = 80, 80

    # -- Create Nodes -- #
    count = 0
    nodes = []

    def create_nodes():
        global count
        for i in range(len(cube_grid)):
            row = []
            for j in range(len(cube_grid[i])):
                node = Node(
                    j * node_width,
                    i * node_height,
                    node_width,
                    node_height,
                    color_dict.get(cube_grid[i][j])[0],
                    count,
                )
                row.append(node)
                count += 1
            nodes.append(row)

    create_nodes()

    possible_moves = [
        up,
        up_prime,
        up_2,
        down,
        down_prime,
        down_2,
        right,
        right_prime,
        right_2,
        left,
        left_prime,
        left_2,
        front,
        front_prime,
        front_2,
        back,
        back_prime,
        back_2,
        up_wide,
        up_wide_prime,
        up_wide_2,
        down_wide,
        down_wide_prime,
        down_wide_2,
        right_wide,
        right_wide_prime,
        right_wide_2,
        left_wide,
        left_wide_prime,
        left_wide_2,
        front_wide,
        front_wide_prime,
        front_wide_2,
        back_wide,
        back_wide_prime,
        back_wide_2,
        x,
        x_prime,
        x_2,
        y,
        y_prime,
        y_2,
        z,
        z_prime,
        z_2,
        middle,
        middle_prime,
        middle_2,
        east,
        east_prime,
        east_2,
        south,
        south_prime,
        south_2,
    ]

    inverse_map = {
        up: up_prime,
        up_prime: up,
        up_2: up_2,
        down: down_prime,
        down_prime: down,
        down_2: down_2,
        right: right_prime,
        right_prime: right,
        right_2: right_2,
        left: left_prime,
        left_prime: left,
        left_2: left_2,
        front: front_prime,
        front_prime: front,
        front_2: front_2,
        back: back_prime,
        back_prime: back,
        back_2: back_2,
        # Wide Moves
        up_wide: up_wide_prime,
        up_wide_prime: up_wide,
        up_wide_2: up_wide_2,
        down_wide: down_wide_prime,
        down_wide_prime: down_wide,
        down_wide_2: down_wide_2,
        right_wide: right_wide_prime,
        right_wide_prime: right_wide,
        right_wide_2: right_wide_2,
        left_wide: left_wide_prime,
        left_wide_prime: left_wide,
        left_wide_2: left_wide_2,
        front_wide: front_wide_prime,
        front_wide_prime: front_wide,
        front_wide_2: front_wide_2,
        back_wide: back_wide_prime,
        back_wide_prime: back_wide,
        back_wide_2: back_wide_2,
        # Rotations
        x: x_prime,
        x_prime: x,
        x_2: x_2,
        y: y_prime,
        y_prime: y,
        y_2: y_2,
        z: z_prime,
        z_prime: z,
        z_2: z_2,
        # Slices
        middle: middle_prime,
        middle_prime: middle,
        middle_2: middle_2,
        east: east_prime,
        east_prime: east,
        east_2: east_2,
        south: south_prime,
        south_prime: south,
        south_2: south_2,
    }

    moves = []
    solve = []

    # -- Parse Arguments -- #
    if len(sys.argv) == 2:
        moves = get_moves_from_file(sys.argv[1])
        solve = [inverse_map[move] for move in reversed(moves)]

    if not moves and len(sys.argv) == 2:
        return

    num_of_moves = 100 if not moves else 1

    # -- Pick Random Moves if none are provided -- #
    if not moves:
        moves = [random.choice(possible_moves) for _ in range(num_of_moves)]
        solve = [inverse_map[move] for move in reversed(moves)]

    # -- Start Pygame -- #

    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 1280, 720
    CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rubik's Cube")
    pywinstyles.change_header_color(None, BLACK[1].lower())

    icon = pygame.image.load("assets/RubiksCubeLogo.png")

    pygame.display.set_icon(icon)

    FPS = 60
    clock = pygame.time.Clock()

    # -- Setup move timer -- #
    move_delay = 100 / num_of_moves
    last_move_time = pygame.time.get_ticks()

    # -- Create Solve Button -- #

    canSolve = False
    solve_btn = SolveButton(CENTER_X - (200 / 2) + 480, CENTER_Y - (200 / 2) + 300, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK[0])

        current_time = pygame.time.get_ticks()

        if moves and current_time - last_move_time > move_delay:
            next_move = moves.pop(0)
            next_move(cube_grid, nodes)
            last_move_time = current_time

        # -- Draw Nodes -- #
        for row in nodes:
            for node in row:
                node.draw(screen)

        if not moves:
            solve_btn.draw(screen)
            solve_btn.on_hover()

        if not canSolve:
            canSolve = solve_btn.on_click()

        if canSolve:
            if not moves:
                if solve and current_time - last_move_time > move_delay:
                    next_move = solve.pop(0)
                    next_move(cube_grid, nodes)
                    last_move_time = current_time
            if not solve:
                solve_btn.done()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
