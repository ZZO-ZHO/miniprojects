# dino RUN
import pygame
import os
import random
pygame.init()

ASSERT = './studyPyGame/Assets/'
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((1100, SCREEN_HEIGHT))
pygame.display.set_caption('Dino RUN !')
icon = pygame.image.load('./studyPyGame/dinorun.png')
pygame.display.set_icon(icon)

BG = pygame.image.load(os.path.join(f'{ASSERT}Other','Track.png'))

RUNNING = [pygame.image.load(f'{ASSERT}Dino/DinoRun1.png'),
           pygame.image.load(f'{ASSERT}Dino/DinoRun2.png')]
DUKINING = [pygame.image.load(f'{ASSERT}Dino/DinoDuck1.png'),
           pygame.image.load(f'{ASSERT}Dino/DinoDuck2.png')]
JUMPING = pygame.image.load(f'{ASSERT}Dino/DinoJump.png')
START = pygame.image.load(f'{ASSERT}Dino/DinoStart.png')
DEAD = pygame.image.load(f'{ASSERT}Dino/DinoDead.png')
# 구름 이미지
CLOUD = pygame.image.load('C:/Source/miniprojects/part1/studyPyGame/Assets/Other/Cloud.png')

BIRD = [pygame.image.load(f'{ASSERT}Bird/Bird1.png'),
        pygame.image.load(f'{ASSERT}Bird/Bird2.png')]

LARGE_CACTUS = [pygame.image.load(f'{ASSERT}Cactus/LargeCactus1.png'),
                pygame.image.load(f'{ASSERT}Cactus/LargeCactus2.png'),
                pygame.image.load(f'{ASSERT}Cactus/LargeCactus3.png')]

SMALL_CACTUS = [pygame.image.load(f'{ASSERT}Cactus/SmallCactus1.png'),
                pygame.image.load(f'{ASSERT}Cactus/SmallCactus2.png'),
                pygame.image.load(f'{ASSERT}Cactus/SmallCactus3.png')]

class Dino: # 공룡 클래스
    X_POS = 80; Y_POS = 310; Y_POS_DUCK = 340; JUMP_VEL = 9.0

    def __init__(self) -> None:
        self.run_img = RUNNING; self.duck_img = DUKINING; self.jump_img = JUMPING
        self.dino_run = True;   self.dino_duck = False;   self.dino_jump = False

        self.step_index = 0
        self.jump_vle = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS


    def update(self, userInput) -> None:
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10: self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:   # 점프
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_rect.y = self.Y_POS   # 공룡이 하늘나는것 방지
        elif userInput[pygame.K_DOWN] and not self.dino_jump:   # 수구리
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not(userInput[pygame.K_DOWN] or self.dino_jump):   # 런
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vle * 4
            self.jump_vle -= 0.8
        if self.jump_vle < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vle = 9.0
        
        self.step_index += 1

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image,(self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self) -> None:
        self.x = SCREEN_WIDTH + random.randint(300, 500)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self) -> None:
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(1300,2000)
            self.y = random.randint(50,100)

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image, (self.x,self.y))

class Obstacle: # 장애물 클래스 (부모클래스)
    def __init__(self, image, type) -> None:
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH  # 1100

    def update(self) -> None:
        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width: # 왼쪽 화면밖으로 벗어나면
            obstacles.pop()

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image[self.type], self.rect)

class Bird(Obstacle):   # 장애물 클래스를 상속
    def __init__(self, image) -> None:
        self.type = 0   # 새는 0 
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0  #0이미지로 시작

    def draw(self, SCREEN) -> None:
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5],self.rect)
        self.index += 1

class LargeCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0,2) # 선인장 세개중 하나 선택
        super().__init__(image,self.type)
        self.rect.y = 300

class SmallCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0,2) # 선인장 세개중 하나 선택
        super().__init__(image,self.type)
        self.rect.y = 3025

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, font
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0

    run = True
    clock = pygame.time.Clock()
    dino = Dino()
    cloud = Cloud()
    game_speed = 14
    obstacles = []
    death_count = 0
    
    font = pygame.font.Font(f'{ASSERT}NanumGothicBold.ttf' , size = 20) # 나중에 나눔고딕으로 변경

    def score():# 함수내 함수
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        txtScore = font.render(f'SCORE : {points}', True, (83,83,83))
        txtRect = txtScore.get_rect()
        txtRect.center = (1000,40)
        SCREEN.blit(txtScore, txtRect)

    def background():   
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))   
        SCREEN.blit(BG, (image_width+x_pos_bg,y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0

        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        background()
        
        score()

        cloud.draw(SCREEN)  # 구름 애니메이션
        cloud.update()

        dino.draw(SCREEN)   # 공룡을 그려준다
        dino.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))
        
        for obs in obstacles:
            obs.draw(SCREEN)
            obs.update()
            if dino.dino_rect.colliderect(obs.rect):
                # pygame.draw.rect(SCREEN, (255,0,0), dino.dino_rect, 3)
                pygame.time.delay(1500)
                death_count += 1
                menu(death_count)

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points, font
    font = pygame.font.Font(f'{ASSERT}NanumGothicBold.ttf' , size = 20) # 나중에 나눔고딕으로 변경
    run = True
    while run:
        SCREEN.fill((255,255,255))

        if death_count == 0:
            text = font.render('시작하려면 아무키나 누르세요.', True,(83,83,83))
            SCREEN.blit(START,(SCREEN_WIDTH // 2 - 20 , SCREEN_HEIGHT // 2 - 140))
        elif death_count > 0:
            text = font.render('재시작하려면 아무키나 누르세요.', True,(83,83,83))
            score = font.render(f'SCORE : {points}', True, (83,83,83))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score,scoreRect)
            SCREEN.blit(DEAD,(SCREEN_WIDTH // 2 - 20 , SCREEN_HEIGHT // 2 - 140))

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()   # 완전종료
            if event.type == pygame.KEYDOWN:
                main()

if __name__ == '__main__':
    menu(death_count = 0)