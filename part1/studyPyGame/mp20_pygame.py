# Python Game - PyGame
# pip install pygame
import pygame

pygame.init()   # 1. 게임 초기화
width = 500; height = 500

win = pygame.display.set_mode((500, 500))   # 윈도우 640*400
pygame.display.set_caption('게임만들기')
icon = pygame.image.load('./studyPyGame/game.png')
pygame.display.set_icon(icon)

# object
x = 250
y = 250 
radius = 10
vel_x = 10
vel_y = 10
vel = 10
jump = False

run = True

while run:
    win.fill((0,0,0))   # 윈도우를 검정으로 채우기
    pygame.draw.circle(win, (255,255,255), (x, y), radius)
    # 이벤트 시그널
    for event in pygame.event.get():    # 2. 이벤트 받기
        if event.type == pygame.QUIT:
            run = False
    
    # 객체이동
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x >= 10:
        x -= vel_x # 왼쪽으로 10씩이동
    if userInput[pygame.K_RIGHT] and x <= width - 10:
        x += vel_x
    # if userInput[pygame.K_UP] and y >= 10:
    #     y -= vel_y
    # if userInput[pygame.K_DOWN] and y <= width - 10:
    #     y += vel_y
    if jump == False and userInput[pygame.K_SPACE]:
        jump = True
    if jump == True:
        y -= vel_y * 3 
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(50)  
    pygame.display.update() # 3. 화면 전환
