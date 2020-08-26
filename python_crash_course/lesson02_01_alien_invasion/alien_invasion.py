import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from button import Button
from game_stats import GameStats
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船、一个子弹组、一个外星人组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环时都重新绘屏幕并让其可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
run_game()