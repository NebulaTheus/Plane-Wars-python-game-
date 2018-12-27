
import time
import pygame
from ship import Ship
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
from pygame.sprite import Group

ai_set=Settings()
def run_game():

    pygame.init()
    screen=pygame.display.set_mode((ai_set.screen_width,ai_set.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship=Ship(ai_set,screen)
    stats=GameStats(ai_set)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(ai_set,screen,aliens)
    play_button=Button(ai_set,screen,'Play')
    sb=Scoreboard(ai_set,screen,stats)
    gf.update_screen(ai_set, screen, ship, bullets, aliens, stats, play_button,sb)

    while True:
       gf.check_events(ai_set,screen,ship,aliens,bullets,stats,play_button,sb)
       if stats.game_active:
           ship.update()
           gf.update_bullets(ai_set,screen,ship,aliens,bullets,stats,sb)
           gf.update_aliens(ai_set,aliens,ship,stats,bullets,screen)
           gf.update_screen(ai_set,screen,ship,bullets,aliens,stats,play_button,sb)
           time.sleep(0.001)


run_game()


