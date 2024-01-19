import pygame
import sys


class Doja:
    def __init__(self):
        self.frame_folders = [
            ['\\back_left', '\\back', '\\back_right'],
            ['\\left', '\\stationary', '\\right'],
            ['\\front_left', '\\front', '\\front_right']
        ]
        self.x, self.y = 1, 1
        self.path = 'Moving_Doja'
        self.gif_frame = 0
        self.image_size = (160, 200)
    def get_direction(self, event):
        keys = pygame.key.get_pressed()

        if all(not key for key in keys):
            self.x = self.y = 1
        elif event.type == pygame.KEYDOWN:
            if keys[pygame.K_a] and keys[pygame.K_w]:
                self.x = 0
                self.y = 0
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                self.x = 2
                self.y = 0
            elif keys[pygame.K_d] and keys[pygame.K_w]:
                self.x = 0
                self.y = 2
            elif keys[pygame.K_d] and keys[pygame.K_s]:
                self.x = 2
                self.y = 2
            elif keys[pygame.K_a]:
                self.x = 1
                self.y = 0
            elif keys[pygame.K_d]:
                self.x = 1
                self.y = 2
            elif keys[pygame.K_w]:
                self.x = 0
                self.y = 1
            elif keys[pygame.K_s]:
                self.x = 2
                self.y = 1
        elif event.type == pygame.KEYUP:
            if (pygame.K_a or pygame.K_d) and (keys[pygame.K_w] or keys[pygame.K_s]):
                self.y = 1
            elif (pygame.K_w or pygame.K_s) and (keys[pygame.K_a] or keys[pygame.K_d]):
                self.x = 1

    def animate(self, screen):
        gif_path = self.path + self.frame_folders[self.x][self.y] + f'\\frame_{self.gif_frame}.png'

        image = pygame.image.load(gif_path)
        image = pygame.transform.scale(image, self.image_size)
        image_rect = image.get_rect()
        image_rect.center = (screen.width / 2, screen.height / 2)

        screen.blit(image, image_rect)

        pygame.display.flip()

        pygame.time.Clock().tick(8)

        if self.gif_frame == 7:
            self.gif_frame = 0
        else:
            self.gif_frame += 1


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('lmao')

    def fill(self, color):
        self.screen.fill(color)

    def blit(self, image, image_rect):
        self.screen.blit(image, image_rect)


# set screen
screen = Screen(1200, 800)

# color
white = (100, 0, 0)

# player
doja = Doja()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()

        doja.get_direction(event)

    screen.fill(white)

    doja.animate(screen)
