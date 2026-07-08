import pygame as pg
from matrix_functions import *

class Camera:

    def __init__(self, sim, position):
        self.render = sim
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.h_fov = math.pi
        self.v_fov = self.h_fov * ()
