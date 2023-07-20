import pygame

from game.utils.constants import LASER,BLACK
from game.components.bursts.burst import Burst
class BulletManager:

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.explosion = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                
                if not game.player.has_power_up:
                    game.playing = False
                    game.death_count -= 1
                    pygame.time.delay(1000)
                    break
        
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    LASER.play()
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 1
                    if game.score > game.high_score:
                        game.high_score = game.score

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)


        for burst in range(9):
            data_burst = 'game/assets/Meteors/explosion{}.png'.format(burst)

            image = pygame.image.load(data_burst).convert()
            image.set_colorkey(BLACK)
            img_scale = pygame.transform.scale(image, (70,70))
            self.explosion.append(img_scale)