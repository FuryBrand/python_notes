class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色RGB。默认是黑色，下面是白色
        self.bg_color = (230, 230, 230)