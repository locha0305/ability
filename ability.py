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
