import random

import pygame as pg
import pygame.display
import sys
import character
import zombie

pg.init()
clock = pg.time.Clock()
wave = 1
zombieWaveCap = 10
totalZombiesSpawned = 0
screen_width = 1472
screen_height = 920
screen = pygame.display.set_mode((screen_width, screen_height))
background = pg.image.load("Background.png")
pygame.mouse.set_visible(False)

last = pg.time.get_ticks()
cooldown = 1500
move_left = False
move_right = False
move_down = False
move_up = False


zombieTest = zombie.Zombie(1452,random.randint(410,480))
spawnedOnLeft = False
myPlayer = character.Player()
all_sprites = pg.sprite.Group()
zombies = pg.sprite.Group()
all_sprites.add(myPlayer)
all_sprites.add(zombieTest)
zombies.add(zombieTest)
layered_group = pg.sprite.LayeredUpdates()


def spawnZombie(spawnedOnLeft):
    if spawnedOnLeft == True:
        newZombie = zombie.Zombie(1452,random.randint(300,440))
        spawnedOnLeft = False
    else:
        newZombie = zombie.Zombie(-200,random.randint(300,440))
        spawnedOnLeft = True
    #all_sprites.add(newZombie)
    #zombies.add(newZombie)
    pg.sprite.LayeredUpdates.add(newZombie)
    layered_group.add(newZombie)

    print("Zombie Spawned")
    return spawnedOnLeft

def handle_move(myPlayer):
    keys = pg.key.get_pressed()

    myPlayer.x_vel = 0
    myPlayer.y_vel = 0
    if keys[pg.K_a]:
        myPlayer.is_moving = True
        myPlayer.direction = "left"
        myPlayer.move_left(8)
    elif keys[pg.K_d]:
        myPlayer.is_moving = True
        myPlayer.direction = "right"
        myPlayer.move_right(8)
    elif keys[pg.K_s]:
        myPlayer.is_moving = True
        myPlayer.move_down(8)
    elif keys[pg.K_w]:
        myPlayer.is_moving = True
        myPlayer.move_up(8)
    else:
        myPlayer.is_moving = False


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    now = pg.time.get_ticks()
    if now - last >= cooldown:
        last = now
        if totalZombiesSpawned <= zombieWaveCap:
                spawnedOnLeft = spawnZombie(spawnedOnLeft)
                totalZombiesSpawned += 1
        else:
            totalZombiesSpawned = 0
            zombieWaveCap += 6
            #Delete after test vvv
            zombieWaveCap = 6
            totalZombiesSpawned = 10
            print("Wave ended")


    myPlayer.loop()
    zombieTest.loop()
    count = 0
    sortedZombies = pg.sprite.LayeredUpdates()
    for x in zombies:
        sortedZombies.add(sorted(zombies, key=lambda x: x.rect.y, reverse=False))
        for y in sortedZombies:
            y._layer += 1
        x.loop()

    # all_sprites.update()
    handle_move(myPlayer)
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    sortedZombies.draw(screen)
    #zombies.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
