import pygame
import os

pygame.init()

# 화면
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()

# 이름, 아이콘
pygame.display.set_caption("Game")
icon = pygame.image.load("C:\\Users\\eyulj\\Desktop\\SandBox\\겜_images\\icon.jpg")
pygame.display.set_icon(icon)

# 폰트
game_font = pygame.font.Font(None, 40)

# 파일 위치
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "겜_images")

##################################################

# background

background = pygame.image.load(os.path.join(images_path, "background.png"))

# Thrower

thrower_img_idx = 0
thrower_img = [
    pygame.image.load(os.path.join(images_path, "Thrower1.png")),
    pygame.image.load(os.path.join(images_path, "Thrower2.png")),
    pygame.image.load(os.path.join(images_path, "Thrower3.png")),
    pygame.image.load(os.path.join(images_path, "Thrower4.png")),
    pygame.image.load(os.path.join(images_path, "Thrower5.png"))
    ]

thrower = thrower_img[thrower_img_idx]
thrower_size = thrower.get_rect().size
thrower_widht = thrower_size[0]  
thrower_height = thrower_size[1]
thrower_posX = 0
thrower_posY = screen_height - thrower_height

# ball

ball = pygame.image.load(os.path.join(images_path, "BlackBaseball.jpg"))
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_posX = 100
ball_posY = screen_height - ball_height

ball_toX = 0
ball_toY = 0
ball_speed = 10

##################################################

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                thrower = thrower_img[thrower_img_idx]
                thrower_img_idx += 1   


##################################################

    screen.blit(background, (0, 0))
    screen.blit(thrower, (thrower_posX, thrower_posY))
    screen.blit(ball, (ball_posX, ball_posY))
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
