import sys
import pygame
from Setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion-Sun')
    # 创建一个外星人、一个飞船、一组子弹编组
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标的事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
