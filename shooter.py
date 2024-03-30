from typing import Any
from pygame import*
from random import randint
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()

back="space.jpg"
hero="rocket1.jpg"
enemy = "roar.png"
bbullet = "patron.png"
lost = 0

window = display.set_mode((700,500))
display.set_caption("ШУТЕР")

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, px, py, size_x, size_y, ps):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_img),(size_x, size_y))
        self.speed = ps
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Play(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(bbullet, self.rect.centerx, self.rect.top, 15,20,-15)
        bullets.add(bullet)

bullets = sprite.Group()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80,620)
            self.rect.y = 0
            lost +=0

ship = Play(hero,5,400,80,100,1)
monsters = sprite.Group()
for i in range(1,6):
    m = Enemy(enemy, randint(80,620), -40, 80,50,randint(1,5))
    monsters.add(m)

finish = False
run = True
background = transform.scale(image.load(back), (700,500))
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        ship.reset()
        ship.update()
        monsters.update()
        monsters.draw(window)


        display.update()


    time.delay(50)

