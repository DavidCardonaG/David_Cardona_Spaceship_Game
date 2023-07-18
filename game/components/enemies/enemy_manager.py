from random import randint
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def add_enemy(self):
        enemy_type = randint(1, 2)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            speed_x = 5
            speed_y = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, speed_x, speed_y, move_x_for)
            
        if len(self.enemies) < 1:
            self.enemies.append(enemy)