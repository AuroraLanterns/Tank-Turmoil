import pygame

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
screen = pygame.display.set_mode((window_width, window_height)) #, pygame.RESIZABLE)  # 如果你希望窗口可调整大小，可以取消注释

# 设置窗口标题
pygame.display.set_caption("Tank Turmoil")
#flag
game_over=False
#坦克类
class Tank_Player:
    def __init__(self,img,x,y,life,speed,skill,deg):
        self.speed=speed
        self.life=life
        self.x=x
        self.y=y
        self.deg=deg
        self.img=pygame.image.load("img/staff_1024.jpg")
        self.skill=skill
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            self.deg -= self.speed
        if keys[pygame.K_RIGHT] :
            self.deg += self.speed
        if keys[pygame.K_up] :
            self.x+=self.speed*cos(pi*self.deg/180)
            self.y+=self.speed*sin(pi*self.deg/180)
        if keys[pygame.K_up] :
            self.x-=self.speed*cos(pi*self.deg/180)
            self.y-=self.speed*sin(pi*self.deg/180)
        
player = Tank_Player()
def draw_player():   
        screen.blit(player.img,(x,y))
# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏逻辑（这里可以添加你的游戏代码）
    # ...

    

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
