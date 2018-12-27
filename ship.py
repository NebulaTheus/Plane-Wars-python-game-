import pygame
class Ship():
    def __init__(self,ai_set,screen,):
        self.screen=screen
        self.ai_set=ai_set
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_left=False
        self.moving_right=False
        self.moving_up=False
        self.moving_down=False
        self.center=float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_set.ship_speed
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center +=self.ai_set.ship_speed
        if self.moving_up and self.rect.top>200:
            self.bottom-=self.ai_set.ship_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.bottom+=self.ai_set.ship_speed

        self.rect.centerx=self.center
        self.rect.bottom=self.bottom

    def center_ship(self):
        self.center=self.screen_rect.centerx
        self.bottom=self.screen_rect.bottom

