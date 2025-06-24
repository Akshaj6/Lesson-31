import pygame
import random
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_CAPTION = "Custom Event - Sprite Color Change"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INITIAL_SPRITE1_COLOR = (255, 0, 0)
INITIAL_SPRITE2_COLOR = (0, 0, 255)
SPRITE_WIDTH = 60
SPRITE_HEIGHT = 60
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)
class ColorChangingSprite(pygame.sprite.Sprite):
    def __init__(self, initial_color, width, height, initial_x, initial_y, name="Sprite"):
        super().__init__()
        self.width = width
        self.height = height
        self.current_color = initial_color
        self.name = name
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.current_color)
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
    def change_color(self):
        new_r = random.randint(0, 255)
        new_g = random.randint(0, 255)
        new_b = random.randint(0, 255)
        self.current_color = (new_r, new_g, new_b)
        self.image.fill(self.current_color)
    def update(self, event):
        if event.type == CHANGE_COLOR_EVENT:
            self.change_color()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)
sprite1 = ColorChangingSprite(
    INITIAL_SPRITE1_COLOR, SPRITE_WIDTH, SPRITE_HEIGHT,
    WINDOW_WIDTH // 4 - SPRITE_WIDTH // 2,
    WINDOW_HEIGHT // 2 - SPRITE_HEIGHT // 2,
    name="Sprite 1"
)
sprite2 = ColorChangingSprite(
    INITIAL_SPRITE2_COLOR, SPRITE_WIDTH, SPRITE_HEIGHT,
    3 * WINDOW_WIDTH // 4 - SPRITE_WIDTH // 2,
    WINDOW_HEIGHT // 2 - SPRITE_HEIGHT // 2,
    name="Sprite 2"
)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(sprite1)
all_sprites_list.add(sprite2)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()