import pygame as p

p.init()
x = 600
y = 600

scrn = p.display.set_mode((x,y))

p.display.set_caption('Matching Game')

color = (220, 20, 60)

scrn.fill(color)

p.display.flip()
status = True

while status:
    for i in p.event.get():
        if i.type == p.QUIT:
            status = False

p.quit()