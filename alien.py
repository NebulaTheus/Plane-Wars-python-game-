import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_set,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_set=ai_set
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>screen_rect.right+40:
            return True
        elif self.rect.left<-40:
            return True
    def update(self):
        self.x+=(self.ai_set.alien_speed*self.ai_set.fleet_direction)
        self.rect.x=self.x
        self.y+=self.ai_set.drop_speed
        self.rect.y=self.y



