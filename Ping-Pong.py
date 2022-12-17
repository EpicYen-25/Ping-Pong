from pygame import *

#parent class for other sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super(). __init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#child class for player
class Paddle (GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

#interface
BLUE = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(BLUE)

#sprites
red_img = "red.png"
blue_img = "paddle_blue.png"
ball_img = "ball.png"

paddleLeft = Paddle (blue_img, 20, 200, 30, 150, 150)
paddleRight = Paddle (red_img, 650, 200, 30, 150, 150)
ball = GameSprite(ball_img, 330, 200, 50, 50, 50)

game = True
finish = False

clock = time.Clock()
FPS = 60

#fonts
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False

    if finish != True:
        window.fill (BLUE)
        paddleLeft.update_left()
        paddleRight.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        paddleLeft.reset()
        paddleRight.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)