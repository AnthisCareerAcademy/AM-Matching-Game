import pygame as p

p.init()

'''This class will be used to create a matching game'''

class MatchingGame:

    #Declares all the variables the class will use
    def __init__(self):
        self.x = 600
        self.y = 600
        self.color = (220, 20, 60)
        self.scrn = p.display.set_mode((self.x,self.y))
        self.status = True
        self.cards_x = [x  for x in range(16)]

    #Creates a new window and set's the color to red
    def create_screen(self):
        p.display.set_caption('MatchingGame')
        self.scrn.fill(self.color)
        p.display.flip()

    #Will be used later to detect action like clicking a card and so on
    def check_condition(self):
        while self.status:
            for i in p.event.get():
                if i.type == p.QUIT:
                    self.status = False
        p.quit()
