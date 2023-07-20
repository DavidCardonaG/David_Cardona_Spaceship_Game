import pygame

from  pygame.sprite import Sprite 


class Burst(Sprite):
    def __init__(self,center,bullet_manager):
        self.image = bullet_manager.explosion[0]
        self.rect = self.image.get_rect()
        self.rect = center
        self.counter = 0
        self.time = pygame.time.get_ticks()
        self.speed = 50



    def update(self,game):
        current = pygame.time.get_ticks()

        if current - self.time > self.speed:
            self.time = current
            self.counter += 1
            if self.counter == len(self.explosion):
                game.reset()
            else:
                center = self.rect
                self.image = self.explosion.append[self.count]
                self.rect = self.image.get_rect()
                self.rect= center


    def draw(self,screen):
        screen.blit(screen.blit(self.image, self.rect))