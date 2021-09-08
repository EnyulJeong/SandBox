import pygame
import os

# 초기화
pygame.init()
pygame.mixer.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Scooter")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 30)

# current path
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Scooter_images")

##################################################

# background
background = pygame.image.load(os.path.join(images_path, "background.jpg"))
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]
background_x1 = 0
background_x2 = background_width
background_speed = 0.4

# scooter
scooter = pygame.image.load(os.path.join(images_path, "scooter.png"))
scooter_size = scooter.get_rect().size
scooter_width = scooter_size[0]
scooter_height = scooter_size[1]
scooter_x = 50
scooter_y = 240

to_x = 0
updown = 0 # 0 이면 위로, 1 이면 아래로
updown_num = 0

song_num = 0
song_play = 0 # 0 이면 무시, 1 이면 재생
song_msg = "by. EnyulJeong"

##################################################

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                song_num += 1
                song_play = 1
        
    # 음악
    if song_play == 1:
        if song_num == 1:
            song_msg = "C418 - Sweden Remix"
            music = 'E:C418 - Sweden Remix.mp3'
        elif song_num == 2:
            song_msg = "Undertale OST - Once Upon A Time"
            music = 'E:Undertale OST - Once Upon A Time.mp3'
        elif song_num == 3:
            song_msg = "Maroon5 - Sunday Morning"
            music = 'E:Maroon5 - Sunday Morning.mp3'
        elif song_num == 4:
            song_msg = "Frank Sinatra - L.O.V.E"
            music = 'E:Frank Sinatra - L.O.V.E.mp3'
            song_num = 0

        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        song_play = 0

    # 배경 속도
    background_x1 -= background_speed * dt
    background_x2 -= background_speed * dt

    # 배경 이어짐
    if background_x1 <= -background_width:
        background_x1 = background_x2 + background_width
    elif background_x2 <= -background_width:
        background_x2 = background_x1 + background_width

    # 스쿠터 움직임
    if scooter_x < 75:
        to_x += 0.0005
    elif scooter_x > 100:
        to_x -= 0.0005

    scooter_x += to_x * dt

    # 스쿠터 진동
    updown_num += 1
    if updown_num % 10 == 0:
        if updown == 0:
            scooter_y += 2
            updown = 1
        elif updown == 1:
            scooter_y -= 2
            updown = 0

    ##################################################

    # 화면
    screen.fill((0, 0, 0)) # 전 song_text 를 덮음
    screen.blit(background,(background_x1, screen_height / 2 - background_height / 2))
    screen.blit(background,(background_x2, screen_height / 2 - background_height / 2))
    screen.blit(scooter, (scooter_x, scooter_y))
    
    # 음악
    song_text = game_font.render(song_msg, True, (255, 255, 255))
    song_rect = song_text.get_rect(topleft = (10, 50))
    screen.blit(song_text, song_rect)

    pygame.display.update()
    
pygame.quit()