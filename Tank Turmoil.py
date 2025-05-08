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
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)  # 如果你希望窗口可调整大小，可以取消注释

# 设置窗口标题
pygame.display.set_caption("Tank Turmoil")
# flag
game_over = False

# 坦克类
class Tank_Player:
    def __init__(self, img, x, y, life, speed, skill, deg):
        self.speed = speed
        self.life = life
        self.x = x
        self.y = y
        self.deg = deg
        self.original_image = pygame.image.load(img)  # 保存原始图片，用于旋转
        self.image = self.original_image  # 当前显示的图片
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # 设置矩形的初始位置
        self.skill = skill

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.deg -= self.speed
        if keys[pygame.K_RIGHT]:
            self.deg += self.speed
        if keys[pygame.K_UP]:
            dx = self.speed * math.cos(math.radians(self.deg))
            dy = self.speed * math.sin(math.radians(self.deg))
            self.x += dx
            self.y += dy
        if keys[pygame.K_DOWN]:
            dx = -self.speed * math.cos(math.radians(self.deg))
            dy = -self.speed * math.sin(math.radians(self.deg))
            self.x += dx
            self.y += dy

        #保持在屏幕内
        self.x = max(0, min(self.x, window_width - self.rect.width))
        self.y = max(0, min(self.y, window_height - self.rect.height))

        self.rect.topleft = (self.x, self.y) #更新rect位置

    def draw(self, screen):
        # 旋转图片
        self.image = pygame.transform.rotate(self.original_image, -self.deg)
        self.rect = self.image.get_rect(center=self.rect.center)  # 更新rect，保持中心位置不变
        screen.blit(self.image, self.rect)  # 绘制旋转后的坦克


# 创建Tank_Player实例时传入所有必需的参数
player = Tank_Player("img/staff_1024.png", 10, 10, 10, 2, "power_up", 0)  # 初始化坦克对象，提供所有参数

# 游戏循环
running = True
clock = pygame.time.Clock() # 添加时钟对象

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            window_width = event.w
            window_height = event.h

    # 更新游戏逻辑
    player.move()
    # ...

    # 绘制背景（可选）
    screen.fill((0, 0, 0))  # 黑色背景

    # 绘制坦克
    player.draw(screen)

    # 更新显示
    pygame.display.flip()
    clock.tick(240) #限制帧率为240

# 退出 Pygame
pygame.quit()
