from pygame import*

mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()

back="space.jpg"
hero="rocket1.jpg"

window = display.set_mode((700,500))
display.set_caption("ШУТЕР")

class Game(sprite.Sprite):
    def __init__(self, player_img, px, py, size_x, size_y, ps):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_img),(size_x, size_y))
        self.speed = ps
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Play(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

ship = Play(hero,5,400,80,100,1)

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


        display.update()


display.update()
time.delay(50)

