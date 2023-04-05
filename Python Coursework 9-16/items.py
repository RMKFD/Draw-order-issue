import pygame as pg

class Pistol(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 200
        self.y_pos = 200
        self.equipped = False
        self.damage = 20
        self.fireRate = 5

