import pygame
from colors import *

text = pygame.font.Font(None, 40)


class SolveButton:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.h = w / (16 / 9)
        self.scale = 10
        self.min_w = self.w
        self.max_w = self.w + 10
        self.color = RED[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.state = "Solve"
        self.hovering = False
        self.canClick = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

        pygame.draw.rect(surface, "white", self.rect, width=2)

        num_surface = text.render(f"{self.state}", True, "white")
        num_rect = num_surface.get_rect()
        num_rect.center = (self.rect.x + (self.w // 2), self.rect.y + (self.h // 2))

        surface.blit(num_surface, num_rect)

    def on_hover(self):
        mouse = pygame.mouse.get_pos()
        if (
            (mouse[0] > self.x and mouse[0] < self.x + self.w)
            and (mouse[1] > self.y and mouse[1] < self.y + self.h)
            and self.state == "Solve"
        ):
            if self.w < self.max_w:
                self.w += self.scale
                self.h = self.w / (16 / 9)
                self.x -= self.scale / 2
                self.y -= self.scale / 2
                self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
                self.hovering = True
            if self.state == "Solve":
                self.color = DARK_RED[0]
            elif self.state == "Solving":
                self.color = DARK_ORANGE[0]
        else:
            if self.w > self.min_w:
                self.w -= self.scale
                self.h = self.w / (16 / 9)
                self.x += self.scale / 2
                self.y += self.scale / 2
                self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            if self.state == "Solve":
                self.color = RED[0]
            elif self.state == "Solving":
                self.color = ORANGE[0]

    def on_click(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if self.hovering and self.state == "Solve":
                if self.canClick:
                    self.canClick = False
                    self.state = "Solving"

                    self.w -= self.scale * 2
                    self.h = self.w / (16 / 9)
                    self.x += self.scale
                    self.y += self.scale
                    self.color = DARKER_RED[0]
                    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

                    return True
        else:
            self.canClick = True

        return False

    def done(self):
        self.color = GREEN[0]
        self.state = "SOLVED"
