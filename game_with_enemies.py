# game_with_enemies.py
#
# Lektionspass 2 (timme 2 - sista kvarten), tisdag 08-april-2025
#
# Robin startade dagen med att koda biblioteket Tkinter
# Detta är hänvisning till biblioteket Flask
#
# Dagens föreläsning blev följande fyra filer
#       ./part1.py          # 1a timmen, med bas i Tkinter
#       ./demo.py           # 1a timmen, med bas i Tkinter
#       ./flaskintro.py             # 2a timmen, med bas i Flask
#       ./templates/index.html      # 2a timmen, med bas i Flask
#
#       ./game.py                   # slutkläm med en enkel spelmotor
#       ./game_with_enemies.py      # ChatGPT förslag på fiender
#  
#
import pygame
import random
import math

pygame.init()

w, h = 400, 400
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
player = pygame.Rect(180, 180, 40, 40)
run = True

# Create some enemies
num_enemies = 5
enemies = [pygame.Rect(random.randint(0, w-20), random.randint(0, h-20), 20, 20) for _ in range(num_enemies)]

def move_toward(rect, target, speed):
    dx = target.x - rect.x
    dy = target.y - rect.y
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    rect.x += int(dx * speed)
    rect.y += int(dy * speed)

while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_UP]: player.y -= 5
    if keys[pygame.K_DOWN]: player.y += 5
    if keys[pygame.K_q]: run = False

    # Move enemies toward player
    for enemy in enemies:
        move_toward(enemy, player, 2)

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 225), player)
    for enemy in enemies:
        pygame.draw.rect(win, (225, 0, 0), enemy)
    pygame.display.flip()

pygame.quit()