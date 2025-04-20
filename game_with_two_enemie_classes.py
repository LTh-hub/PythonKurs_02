# game_with_two_enemie_classes.py
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
#       ./templates/about.html      # Egen laboration efter lektion
#       ./templates/mitt_foto.html  # Egen laboration efter lektion
#
#       ./game.py                   # slutkläm med en enkel spelmotor
#       ./game_with_enemies.py      # ChatGPT förslag på fiender
#       ./game_with_two_enemie_classes.py      # ChatGPT förslag på fler fiender # Egen laboration efter lektion
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

# Röda rektangelfiender
num_enemies = 5
enemies = [pygame.Rect(random.randint(0, w-20), random.randint(0, h-20), 20, 20) for _ in range(num_enemies)]

# Gula triangelfiender (använder dict för att lagra position)
num_triangle_enemies = 3
triangles = [{'x': random.randint(0, w), 'y': random.randint(0, h)} for _ in range(num_triangle_enemies)]

def move_toward_rect(rect, target, speed):
    dx = target.x - rect.x
    dy = target.y - rect.y
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    rect.x += int(dx * speed)
    rect.y += int(dy * speed)

def move_toward_point(enemy, target_rect, speed):
    dx = target_rect.centerx - enemy['x']
    dy = target_rect.centery - enemy['y']
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    enemy['x'] += dx * speed
    enemy['y'] += dy * speed

def draw_triangle(surface, x, y, size, color):
    points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
    pygame.draw.polygon(surface, color, points)

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

    for enemy in enemies:
        move_toward_rect(enemy, player, 2)
    for tri in triangles:
        move_toward_point(tri, player, 1.5)

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 225), player)
    for enemy in enemies:
        pygame.draw.rect(win, (225, 0, 0), enemy)
    for tri in triangles:
        draw_triangle(win, tri['x'], tri['y'], 10, (255, 215, 0))  # gul färg

    pygame.display.flip()

pygame.quit()