import pygame

pygame.font.init()

num = pygame.font.Font(None, 20)


class Node:
    def __init__(self, x, y, w, h, color, number):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.number = number

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

        if self.color != (0, 0, 0):
            pygame.draw.rect(surface, "white", self.rect, width=2)

            num_surface = num.render(f"{self.number}", True, "white")
            num_rect = num_surface.get_rect()
            num_rect.center = (self.rect.x + (self.w // 2), self.rect.y + (self.h // 2))

            # ENABLE to see cube id numbers
            # surface.blit(num_surface, num_rect)

        # ENABLE to see cube grid
        # pygame.draw.rect(surface, "white", self.rect, width=2)
