class Settings():
    def __init__(self):
        self.screen_width=800   #游戏窗口尺寸
        self.screen_height=600
        self.bg_color=0,0,0    #背景颜色
        self.bullet_width=3    #子弹宽度
        self.bullet_height=15  #子弹长度
        self.bullet_color=255,255,0
        self.bullet_allowed=8   #最多同时存在子弹数量
        self.ship_limit=3       #几条命
        self.speedup_scale=1.2  #游戏加速倍率
        self.init_set()

    def init_set(self):
        self.ship_speed = 1        #飞船速度
        self.bullet_speed = 1      #子弹速度
        self.alien_speed = 0.5     #外星人左右移速
        self.drop_speed = 0.1      #外星人下降速度
        self.fleet_direction = 1   #标志位，用以控制左移还是右移

    def speedup(self):        #消灭一波外星人后加速
        self.ship_speed *=self.speedup_scale
        self.bullet_speed *=self.speedup_scale
        self.alien_speed *=self.speedup_scale
        self.drop_speed *=self.speedup_scale




