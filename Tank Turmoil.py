import pygame
import math  # 导入sin, cos, pi

# 初始化 Pygame
pygame.init()

# 获取屏幕信息
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# 计算窗口尺寸
window_width = int(screen_width * 0.3)
window_height = int(screen_height * 0.8)

# 创建窗口 
screen = pygame.display.set_mode((window_width, window_height) ,pygame.RESIZABLE)  # 如果你希望窗口可调整大小，可以取消注释

# 设置窗口标题
pygame.display.set_caption("Tank Turmoil")
#flag
game_over=False
#坦克类
class Tank_Player:
    def __init__(self, img, x, y, life, speed, skill, deg):
        self.speed = speed
        self.life = life
        self.x = x
        self.y = y
        self.deg = deg
        self.img = pygame.image.load(img)  # 使用传入的img路径加载图片
        self.skill = skill

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.deg -= self.speed
        if keys[pygame.K_RIGHT]:
            self.deg += self.speed
        if keys[pygame.K_UP]:
            self.x += self.speed * cos(pi * self.deg / 180)
            self.y += self.speed * sin(pi * self.deg / 180)
        if keys[pygame.K_DOWN]:  # 修改K_up为K_DOWN
            self.x -= self.speed * cos(pi * self.deg / 180)
            self.y -= self.speed * sin(pi * self.deg / 180)
        

def draw_player(player):   
    screen.blit(player.img, (player.x, player.y))  # 绘制坦克图像到屏幕上

# 创建Tank_Player实例时传入所有必需的参数
player = Tank_Player("img/staff_1024.png", 10, 10, 10, 2, "power_up", 0)  # 初始化坦克对象，提供所有参数

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏逻辑
    player.move()
    # ...

    # 绘制背景（可选）
    screen.fill((0, 0, 0))  # 黑色背景

    # 绘制坦克
    draw_player(player)

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
