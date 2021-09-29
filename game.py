# 操控 sprite
import pygame
W = 500
H = 600
FPS = 60
white = (255, 255, 255)
GREEN = (0 , 255, 0)


# game initializ ation
pygame.init()
screan = pygame.display.set_mode((W, H)) #set screan size
pygame.display.set_caption('First game')
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (W/2)
        self.rect.bottom = H - 10
        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()# 回傳布林直 控制鍵盤
        if key_pressed[pygame.K_RIGHT]: # 判斷右鍵有沒有觸發
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]: # 判斷左鍵鍵有沒有觸發
            self.rect.x -= self.speedx
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)




running = True

while running:
    clock.tick(FPS) # limit loop times FPS

    #Get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

 
    #display
    screan.fill((white)) # Adjust color use rgb
    all_sprites.draw(screan)
    pygame.display.update()
pygame.quit()
