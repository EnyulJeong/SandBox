import pygame
import os

pygame.init()

# 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()

# 이름, 아이콘
pygame.display.set_caption("Tiles")
# icon = pygame.image.load("C:\\Users\\eyulj\\Desktop\\SandBox\\tiles_images\\icon.jpg")
# pygame.display.set_icon(icon)

# 폰트
game_font = pygame.font.Font(None, 40)

# 파일 위치
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "tiles_images")

##################################################

# tile

tile = pygame.image.load("C:\\Users\\eyulj\\Desktop\\SandBox\\tiles_images\\tile.png")
tile_size = tile.get_rect().size
tile_width = tile_size[0]
tile_height = tile_size[1]
tile_posX = 0
tile_posY = 0

tile_toY = 0
tile_speed = 0.01

# board

board = pygame.image.load("C:\\Users\\eyulj\\Desktop\\SandBox\\tiles_images\\board.png")
board_size = board.get_rect().size
board_width = board_size[0]
board_height = board_size[1]
board_posX = screen_width / 8
board_posY = screen_height - tile_height


##################################################

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a")
            elif event.key == pygame.K_s:
                print("b")
            elif event.key == pygame.K_d:
                print("c")
            elif event.key == pygame.K_f:
                print("f")
            elif event.key == pygame.K_j:
                print("j")
            elif event.key == pygame.K_k:
                print("k")
            elif event.key == pygame.K_l:
                print("l")
            elif event.key == pygame.K_SEMICOLON:
                print(";")

    tile_toY += tile_speed * dt
    tile_posY += tile_toY

##################################################

    screen.fill((0, 0, 0))
    screen.blit(tile, (tile_posX, tile_posY))
    for n in range(0, 8):
        posX_idx = n
        screen.blit(board, (board_posX * posX_idx, board_posY))
    pygame.display.update()

pygame.quit()

# pygame 종료
pygame.quit()