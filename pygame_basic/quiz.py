import random
from turtle import back, screensize
from numpy import char, character
import pygame

pygame.init

# 화면 설정
screen_width = 480
screent_height = 640
screen = pygame.display.set_mode((screen_width, screent_height))

pygame.display.set_caption("Quiz")

clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경
background = pygame.image.load("C:/Users/CHAMDAHAN/Desktop/Git/Git-Python/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/CHAMDAHAN/Desktop/Git/Git-Python/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
charcter_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screent_height - character_height

# 이동 위치
to_x = 0
character_spped = 10

# 똥 만들기
ddong = pygame.image.load("C:/Users/CHAMDAHAN/Desktop/Git/Git-Python/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


