import pygame
import math

def set_fps(Fps):
    global fps
    fps = Fps

class Entity():
    global fps
    def __init__(self, summon_x, summon_y, max_hp, max_mp, image):
        self.x = summon_x
        self.y = summon_y
        self.dx = 0
        self.dy = 0
        self.dir = None
        self.hp = max_hp
        self.mp = max_mp
        self.image = pygame.image.load(image)
        
        self.skill = []
        self.skill_mp = []
        self.skill_cooltime = []
        self.skill_max_cooltime = []
    def goto(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    def advance(self):
        self.x += self.dx
        self.y += self.dy
    def attach(self, skill_name):
        self.skill.append(skill_name)
        self.skill_cooltime.append(skill_name.cooltime)
        self.skill_max_cooltime.append(skill_name.cooltime)
    def detach(self, skill_name):
        skill_index = self.skill_name.index(skill_name)
        del self.skill_name[skill_index]
        del self.skill_mp[skill_index]
        del self.skill_cooltime[skill_index]
        del self.skill_max_cooltime[skill_index]
    def collide_entity(self, entity_name):
        self.hitbox = self.image.get_rect()
        self.hitbox.left = self.x
        self.hitbox.top = self.y

        entity_hitbox = entity_name.image.get_rect()
        entity_hitbox.left = entity_name.x
        entity_hitbox.top = entity_name.y

        if self.hitbox.colliderect(entity_hitbox):
            return True
        else:
            return False
    def collide_projectile(self, projectile_name):
        self.hitbox = self.image.get_rect()
        self.hitbox.left = self.x
        self.hitbox.top = self.y
        for positions in projectile_name.position:
            projectile_x = positions[0]
            projectile_y = positions[1]
            projectile_hitbox = projectile_name.image.get_rect()
            projectile_hitbox.left = projectile_x
            projectile_hitbox.top = projectile_y
            if self.hitbox.colliderect(projectile_hitbox):
                return True
            else:
                pass
        return False
    def use_skill(self, skill_name):
        skill_index = self.skill_name.index(skill_name)
        skill_name.active()
        self.mp -= skill_name.mp
        self.skill_cooltime[skill_index] = self.skill_max_cooltime[skill_index]
    def active_cooltime_tick(self):
        for skill_index in range(0, len(self.skill_cooltime)):
            cooltime = self.skill_cooltime[skill_index]
            if cooltime - fps > 0:
                self.skill_cooltime[skill_index] -= fps
            else:
                self.skill_cooltime[skill_index] = 0
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
        

class Projectile():
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.position = []
        self.dx = 0
        self.dy = 0
    def add(self, x_pos, y_pos, Dir):
        self.position.append([x_pos, y_pos, Dir])
    def destory(self, projectile_index):
        del self.position[projectile_index]
    def goto(self, projectile_index, x_pos, y_pos):
        self.position[projectile_index][0] = x_pos
        self.position[projectile_index][1] = y_pos
    def advance(self):
        for position_index in range(0, len(self.position)):
            Dir = self.position[position_index][2]
            if Dir == 1:
                self.position[position_index][0] += self.dx
                self.position[position_index][1] += self.dy
            else:
                self.position[position_index][0] -= self.dx
                self.position[position_index][1] -= self.dy
            
    def draw(self, screen):
        for positions in self.position:
            x_pos = positions[0]
            y_pos = positions[1]

            screen.blit(self.image, (x_pos, y_pos))
