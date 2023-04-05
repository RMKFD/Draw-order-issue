import pygame as pg

import character
#from main import myPlayer


class Zombie(pg.sprite.Sprite):
    def __init__(self,xSpawn,ySpawn):
        super().__init__()
        self.x_pos = xSpawn
        self.y_pos = ySpawn
        self.x_vel = 0
        self.y_vel = 0
        self.is_moving = False
        self.direction = "right"
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.last = pg.time.get_ticks()
        self.cooldown = 1000
        self._layer = 0


#Idle Right
        self.ZombieIdle = []
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right00.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right01.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right02.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right03.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right04.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right05.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right06.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right07.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right08.png"))
        self.ZombieIdle.append(pg.image.load("Zombie Idle/Zombie1 Idle Right09.png"))
        self.current_sprite = 0


#Idle Left
        self.ZombieIdleLeft = []
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right00.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right01.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right02.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right03.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right04.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right05.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right06.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right07.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right08.png"),True, False))
        self.ZombieIdleLeft.append(pg.transform.flip(pg.image.load("Zombie Idle/Zombie1 Idle Right09.png"),True, False))
        self.current_sprite = 0






#Moving Right
        self.ZombieRight = []
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right00.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right01.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right02.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right03.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right04.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right05.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right06.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right07.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right08.png"))
        self.ZombieRight.append(pg.image.load("Zombie Right/Zombie1 Right09.png"))
        self.current_sprite = 0

#Moving Left
        self.ZombieLeft = []
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right00.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right01.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right02.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right03.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right04.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right05.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right06.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right07.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right08.png"), True, False))
        self.ZombieLeft.append(pg.transform.flip(pg.image.load("Zombie Right/Zombie1 Right09.png"), True, False))
        self.current_sprite = 0


        if self.is_moving == False:
            if self.direction == "right":
                self.image = self.ZombieIdle[self.current_sprite]
                self.rect = self.image.get_rect().move(xSpawn,ySpawn)
            elif self.direction == "left":
                self.image = self.ZombieIdleLeft[self.current_sprite]
                self.rect = self.image.get_rect().move(xSpawn,ySpawn)


        elif self.is_moving == True:
            if self.direction == "right":
                self.image = self.ZombieRight[self.current_sprite]
                self.rect = self.image.get_rect().move(xSpawn,ySpawn)
            elif self.direction == "left":
                self.image = self.ZombieLeft[self.current_sprite]
                self.rect = self.image.get_rect().move(xSpawn,ySpawn)


    def update(self):
        if self.is_moving == False:
            if self.direction == "right":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.ZombieIdle):
                    self.current_sprite = 0

                self.image = self.ZombieIdle[int(self.current_sprite)]

            elif self.direction == "left":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.ZombieIdleLeft):
                    self.current_sprite = 0

                self.image = self.ZombieIdleLeft[int(self.current_sprite)]

        elif self.is_moving == True:

            if self.direction == "right":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.ZombieRight):
                    self.current_sprite = 0

                self.image = self.ZombieRight[int(self.current_sprite)]

            elif self.direction == "left":
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.ZombieLeft):
                    self.current_sprite = 0

                self.image = self.ZombieLeft[int(self.current_sprite)]

        # if self.rect.x >= 1260:
        #     self.x_vel = -5
        # elif self.rect.x <= 1:
        #     self.x_vel = 5
        #
        # if self.rect.y >= 750:
        #     self.y_vel = -5
        # elif self.rect.y <= 10:
        #     self.y_vel = 5
        from main import myPlayer


        if self.rect.x == myPlayer.rect.x:
            if self.rect.y > myPlayer.rect.y:
                self.move_up(1)
            else:
                self.move_down(1)
        elif self.rect.y == myPlayer.rect.y:
            if self.rect.x > myPlayer.rect.x:
                self.move_left(1)
            else:
                self.move_right(1)
        elif self.rect.x > myPlayer.rect.x + 30:
            self.move_left(1)
        elif self.rect.x < myPlayer.rect.x - 30:
            self.move_right(1)

        elif self.rect.y > myPlayer.rect.y + 30:
            self.move_up(1)
        elif self.rect.y < myPlayer.rect.y - 30:
            self.move_down(1)

        if self.rect.x in range(myPlayer.rect.x,myPlayer.rect.x + 30):
            if self.rect.y in range(myPlayer.rect.y,myPlayer.rect.y + 30 ):
                self.hit()
            elif self.rect.y in range(myPlayer.rect.y,myPlayer.rect.y - 30):
                self.hit()
        elif self.rect.x in range(myPlayer.rect.x,myPlayer.rect.x - 30):
            if self.rect.y in range(myPlayer.rect.y, myPlayer.rect.y + 30):
                self.hit()
            elif self.rect.y in range(myPlayer.rect.y, myPlayer.rect.y - 30):
                self.hit()







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

    def hit(self):
        now = pg.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.isAttacking = True
            from main import myPlayer
            myPlayer.currentHealth - 20


