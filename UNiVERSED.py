import pygame

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("UNiVERSED")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

##################################################

