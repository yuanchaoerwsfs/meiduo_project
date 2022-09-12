import sys
import pygame
from bullet import Bullet
from Alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # 飞船向右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 飞船向左移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹。并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def check_events(ai_settings, screen, ship, bullets):
    """响应案件和鼠标的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.darw_bullet()
    ship.blitme()  # 指定位置绘画出飞船图标
    aliens.draw(screen)  # 指定位置绘画出外星人图标
    pygame.display.flip()  # 让最近绘画的图案可见


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到子弹上限，那么就新创建一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()  # 刷新子弹显示位置,并删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # 可通过配置两个参数改变子弹消失效果，False，True
    if len(aliens) == 0:
        # 删除现有的子弹并建立新的一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """计算X方向能够容纳多少个外星人"""
    available_alien_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_alien_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算Y方向屏幕中能容纳多少行外星人"""
    print(alien_height)
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2.5 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人，并把它放在当前行位置"""
    alien = Alien(alien_number, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():  # 检查是否有外星人到达或超出边界，如果有返回True
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        print("Ship hit !!")
    # 检查是否有外星人到达底部
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人装到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left = -1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
