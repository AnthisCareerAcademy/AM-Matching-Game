import pygame as p

p.init()

class MatchingGame:

    def __init__(self):
        self.x = 600
        self.y = 600
        self.color = (220, 20, 60)
        self.scrn = p.display.set_mode((self.x,self.y))
        self.status = True


    def create_screen(self):
        p.display.set_caption('MatchingGame')
        self.scrn.fill(self.color)
        p.display.flip()


    def check_condition(self):
        while self.status:
            for i in p.event.get():
                if i.type == p.QUIT:
                    self.status = False
        p.quit()
