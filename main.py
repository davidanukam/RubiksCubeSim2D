import os, contextlib

with contextlib.redirect_stdout(None):
    import pygame as pg


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


import sys, pywinstyles, keyboard, random
from collections.abc import Callable
from typing import Any
from utils.colors import *
from utils.movement import *
from node import Node
from solve_button import SolveButton
from utils.cube_data import cube_grid
from utils.file_parser import get_moves_from_file
from object_3d import *


class Simulation:
    def __init__(self):
        # -- Exit if too many arguments are passed -- #
        if len(sys.argv) > 2:
            print("\n***** ERROR: Too many arguments! *****")
            print("\nUsage: python main.py [<file_name>]")
            return

        pg.init()
        pg.font.init()

        keyboard.block_key("windows")

        self.WIDTH, self.HEIGHT = 1280, 720
        self.CENTER_X, self.CENTER_Y = self.WIDTH // 2, self.HEIGHT // 2

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Rubik's Cube Simulation")
        pywinstyles.change_header_color(self.screen, BLACK[1].lower())

        self.icon = pg.image.load(resource_path("assets/RubiksCubeLogo.png"))
        pg.display.set_icon(self.icon)

        self.FPS = 60
        self.clock = pg.time.Clock()

        # --  Node Variables -- #
        self.node_width, self.node_height = 80, 80

        # -- Create Nodes -- #
        self.count = 0
        self.nodes: list[list[Node]] = []
        self.create_nodes()

        # -- Move Mappings -- #
        self.possible_moves = [
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

        self.inverse_map = {
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

        # (Alt, Shift, Ctrl) combinations
        self.MOVE_MAPPING = {
            # Alt + Shift = Wide Prime moves
            (True, True, False): {
                pg.K_r: right_wide_prime,
                pg.K_l: left_wide_prime,
                pg.K_u: up_wide_prime,
                pg.K_d: down_wide_prime,
                pg.K_f: front_wide_prime,
                pg.K_b: back_wide_prime,
            },
            # Alt + Ctrl = Wide Twice moves
            (True, False, True): {
                pg.K_r: right_wide_2,
                pg.K_l: left_wide_2,
                pg.K_u: up_wide_2,
                pg.K_d: down_wide_2,
                pg.K_f: front_wide_2,
                pg.K_b: back_wide_2,
            },
            # Alt only = Wide moves
            (True, False, False): {
                pg.K_r: right_wide,
                pg.K_l: left_wide,
                pg.K_u: up_wide,
                pg.K_d: down_wide,
                pg.K_f: front_wide,
                pg.K_b: back_wide,
            },
            # Shift only = Basic Prime moves
            (False, True, False): {
                pg.K_r: right_prime,
                pg.K_l: left_prime,
                pg.K_u: up_prime,
                pg.K_d: down_prime,
                pg.K_f: front_prime,
                pg.K_b: back_prime,
                pg.K_x: x_prime,
                pg.K_y: y_prime,
                pg.K_z: z_prime,
                pg.K_m: middle_prime,
                pg.K_e: east_prime,
                pg.K_s: south_prime,
            },
            # Ctrl only = Basic Twice moves
            (False, False, True): {
                pg.K_r: right_2,
                pg.K_l: left_2,
                pg.K_u: up_2,
                pg.K_d: down_2,
                pg.K_f: front_2,
                pg.K_b: back_2,
                pg.K_x: x_2,
                pg.K_y: y_2,
                pg.K_z: z_2,
                pg.K_m: middle_2,
                pg.K_e: east_2,
                pg.K_s: south_2,
            },
            # No modifiers = Basic moves
            (False, False, False): {
                pg.K_r: right,
                pg.K_l: left,
                pg.K_u: up,
                pg.K_d: down,
                pg.K_f: front,
                pg.K_b: back,
                pg.K_x: x,
                pg.K_y: y,
                pg.K_z: z,
                pg.K_m: middle,
                pg.K_e: east,
                pg.K_s: south,
            },
        }

        self.moves: list[Callable[..., Any]] = []
        # self.solve = []

        # -- Setup move timer -- #
        self.move_delay = 1  # / num_of_moves
        self.last_move_time = pg.time.get_ticks()

        # -- Create Solve Button -- #
        # self.canSolve = False
        # self.solve_btn = SolveButton(CENTER_X - (200 / 2) + 480, CENTER_Y - (200 / 2) + 300, 200)

        """ # LEGACY CUBE SOLVER (INVERSE MAPPING)
        # -- Parse Arguments -- #
        if len(sys.argv) == 2:
            file_to_open = os.path.abspath(sys.argv[1])
            moves = get_moves_from_file(file_to_open)
            solve = [inverse_map[move] for move in reversed(moves)]

        if not moves and len(sys.argv) == 2:
            return

        num_of_moves = 100 if not moves else 1

        # -- Pick Random Moves if none are provided -- #
        if not moves:
            moves = [random.choice(possible_moves) for _ in range(num_of_moves)]
            solve = [inverse_map[move] for move in reversed(moves)]
        """

        # NOTE: Testing 3D rendering below #

        def create_objects():
            object = Object3D(self)

        self.moves = [random.choice(self.possible_moves) for _ in range(100)]

    def create_nodes(self):
        for i in range(len(cube_grid)):
            row: list[Node] = []
            for j in range(len(cube_grid[i])):
                node = Node(
                    j * self.node_width,
                    i * self.node_height,
                    self.node_width,
                    self.node_height,
                    color_dict.get(cube_grid[i][j])[0],
                    self.count,
                )
                row.append(node)
                self.count += 1
            self.nodes.append(row)

    def update(self):
        # -- Move Animation -- #
        self.current_time = pg.time.get_ticks()
        if self.moves and self.current_time - self.last_move_time > self.move_delay:
            next_move = self.moves.pop(0)
            next_move(cube_grid, self.nodes)
            self.last_move_time = self.current_time

    def draw(self):
        self.screen.fill(BLACK[0])

        for row in self.nodes:
            for node in row:
                node.draw(self.screen)

        pg.display.flip()

    def run(self):
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    is_alt = bool(event.mod & pg.KMOD_ALT)
                    is_shift = bool(event.mod & pg.KMOD_SHIFT)
                    is_ctrl = bool(event.mod & pg.KMOD_CTRL)

                    mod_combo = (is_alt, is_shift, is_ctrl)

                    current_key_map = self.MOVE_MAPPING.get(mod_combo, {})

                    if event.key in current_key_map:
                        self.moves.append(current_key_map[event.key])

            self.update()

            self.draw()

            # -- Solve Button -- #
            # if not self.moves:
            #     self.solve_btn.draw(self.screen)
            #     self.solve_btn.on_hover()

            # if not self.canSolve:
            #     self.canSolve = self.solve_btn.on_click()

            # if self.canSolve:
            #     if not self.moves:
            #         if self.solve and self.current_time - self.last_move_time > self.move_delay:
            #             next_move = self.solve.pop(0)
            #             next_move(cube_grid, self.nodes)
            #             self.last_move_time = self.current_time
            #     if not self.solve:
            #         self.solve_btn.done()

            self.clock.tick(self.FPS)

        pg.quit()
        sys.exit()


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
