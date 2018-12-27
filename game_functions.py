import sys
import pygame
from bullet import Bullet
from alien import Alien
import time

def check_keydown(ai_set,screen,event,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets)<ai_set.bullet_allowed:
            new_bullet=Bullet(ai_set,screen,ship)
            bullets.add(new_bullet)

def check_keyup(ai_set,screen,event,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_set,screen,ship,aliens,bullets,stats,play_button,sb):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown(ai_set,screen,event,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(ai_set,screen,event,ship,bullets)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_set,screen,ship,sb)

def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_set,screen,ship,sb):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        ai_set.init_set()
        stats.reset_start()
        sb.prep_score()
        stats.game_active=True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_set,screen,aliens)
        ship.center_ship()





def update_screen(ai_set,screen,ship,bullets,aliens,stats,play_button,sb):  # update screen 刷新屏幕
    screen.fill(ai_set.bg_color)
    aliens.draw(screen)
    ship.blitme()
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()



    pygame.display.flip()

def update_bullets(ai_set,screen,ship,aliens,bullets,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_set,screen,ship,aliens,bullets,stats,sb)


def check_bullet_alien_collisions(ai_set,screen,ship,aliens,bullets,stats,sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=len(aliens)
            sb.prep_score()

    if len(aliens)==0:
        bullets.empty()
        ai_set.speedup()
        create_fleet(ai_set,screen,aliens)



def get_number(ai_set,alien_width):
    avaliable_x=ai_set.screen_width-2*alien_width
    number=int(avaliable_x/(1.5*alien_width))
    # print(avaliable_x,alien_width,number)
    return(number)

def create_alien(ai_set,screen,aliens,alien_number,row_number):
    alien=Alien(ai_set,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+1.5*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height*(1+2*row_number)
    alien.y=alien.rect.height*(1+2*row_number)
    aliens.add(alien)

def create_fleet(ai_set,screen,aliens):
    alien=Alien(ai_set,screen)
    number=get_number(ai_set,alien.rect.width)
    for row_number in range(3):  #外星人行数
        for alien_num in range(number): #公众号：老王的小船
            create_alien(ai_set,screen,aliens,alien_num,row_number)

def check_fleet_edges(ai_set,aliens,screen):
    for alien in aliens.sprites():
        if check_alien_bottom(screen,alien):
            aliens.remove(alien)
        if alien.check_edges():
            change_fleet_direction(ai_set,aliens)
            break


def change_fleet_direction(ai_set,aliens):
    ai_set.fleet_direction*=-1

def check_alien_bottom(screen,alien):
    screen_rect=screen.get_rect()
    if alien.rect.top>screen_rect.bottom:
        return True

def update_aliens(ai_set,aliens,ship,stats,bullets,screen):
    check_fleet_edges(ai_set,aliens,screen)
    aliens.update()
    if pygame.sprite.spritecollide(ship,aliens,False):
        ship_hit(stats,ship,bullets)


def ship_hit(stats,ship,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        bullets.empty()
        ship.center_ship()
        time.sleep(0.3)
    else:
        stats.game_active=False
