# game.py
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
pygame.init()

w, h = 400, 400
win = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
player = pygame.Rect(180, 180, 40,40)
run = True

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
    
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 225), player)
    pygame.display.flip()

pygame.quit()


