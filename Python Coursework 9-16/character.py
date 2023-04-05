import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 200
        self.y_pos = 200
        self.x_vel = 0
        self.y_vel = 0
        self.is_moving = False
        self.direction = "right"
        self.maxHealth = 100
        self.currentHealth = 100



#Idle Right
        self.JakeIdle = []
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-1.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-2.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-3.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-4.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-5.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-6.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-7.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-8.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-9.png"))
        self.JakeIdle.append(pg.image.load("Jake Idle/Jake Idle-10.png"))
        self.current_sprite = 0


#Idle Left
        self.JakeIdleLeft = []
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-1.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-2.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-3.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-4.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-5.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-6.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-7.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-8.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-9.png"), True, False))
        self.JakeIdleLeft.append(pg.transform.flip(pg.image.load("Jake Idle/Jake Idle-10.png"), True, False))





#Moving Right
        self.JakeRight = []
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-1.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-2.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-3.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-4.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-5.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-6.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-7.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-8.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-9.png"))
        self.JakeRight.append(pg.image.load("Jake Right/Jake Right-10.png"))
        self.current_sprite = 0

#Moving Left
        self.JakeLeft = []

        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-1.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-2.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-3.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-4.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-5.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-6.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-7.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-8.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-9.png"), True, False))
        self.JakeLeft.append(pg.transform.flip(pg.image.load("Jake Right/Jake Right-10.png"), True, False))
        self.current_sprite = 0


        if self.is_moving == False:
            if self.direction == "right":
                self.image = self.JakeIdle[self.current_sprite]
                self.rect = self.image.get_rect().move(200,200)
            elif self.direction == "left":
                self.image = self.JakeIdleLeft[self.current_sprite]
                self.rect = self.image.get_rect().move(200,200)


        elif self.is_moving == True:
            if self.direction == "right":
                self.image = self.JakeRight[self.current_sprite]
                self.rect = self.image.get_rect().move(200,200)
            elif self.direction == "left":
                self.image = self.JakeLeft[self.current_sprite]
                self.rect = self.image.get_rect().move(200,200)





    def update(self):
        print(self.currentHealth , "/" , self.maxHealth)
        if self.is_moving == False:
            if self.direction == "right":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.JakeIdle):
                    self.current_sprite = 0

                self.image = self.JakeIdle[int(self.current_sprite)]

            elif self.direction == "left":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.JakeIdleLeft):
                    self.current_sprite = 0

                self.image = self.JakeIdleLeft[int(self.current_sprite)]

        elif self.is_moving == True:

            if self.direction == "right":
                self.current_sprite += 0.4

                if self.current_sprite >= len(self.JakeRight):
                    self.current_sprite = 0

                self.image = self.JakeRight[int(self.current_sprite)]

            elif self.direction == "left":
                self.current_sprite += 0.4

                if self.current_sprite >= len(self.JakeLeft):
                    self.current_sprite = 0

                self.image = self.JakeLeft[int(self.current_sprite)]

        if self.rect.x >= 1260:
            self.x_vel = -5
        elif self.rect.x <= 1:
            self.x_vel = 5

        if self.rect.y >= 750:
            self.y_vel = -5
        elif self.rect.y <= 10:
            self.y_vel = 5


    def move(self, disx, disy):
        self.is_moving = True
        self.rect.x += disx
        self.rect.y += disy

    def move_left(self, vel):
        self.is_moving = True
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"

    def move_right(self, vel):
        self.is_moving = True
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"

    def move_down(self, vel):
        self.is_moving = True
        self.y_vel = vel

    def move_up(self, vel):
        self.is_moving = True
        self.y_vel = -vel

    def loop(self):
        self.move(self.x_vel, self.y_vel)
        self.is_moving = True




