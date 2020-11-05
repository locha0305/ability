import pygame
import math

def set_fps(Fps):
    global fps
    fps = Fps

def mainloop(All_Entity, All_Projectile, screen, x_pos, y_pos):
    global fps
    for Entities in All_Entity.Entities:
        if Entities.hp <= 0:
            if Entities in All_Entity.Entities:
                Entities.goto(x_pos, y_pos)
                All_Entity.destory(Entities)
            else:
                pass
        else:
            pass

    All_Entity.draw(screen)
    All_Projectile.draw(screen)

    All_Entity.advance()
    All_Projectile.advance()

    All_Entity.active_cooltime_tick()

    pygame.display.update()


class Entity():
    global fps
    def __init__(self, summon_x, summon_y, max_hp, max_mp, image, All_Entity):
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
        All_Entity.add(self)
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
        print("{}: {}".format(self.skill.index(skill_name) + 1, skill_name.name))
        print("===================")
        print("mp :{}, cooltime: {}초\n".format(skill_name.mp, skill_name.cooltime / 1000))
        print(skill_name.description)
        print("===================\n")
    def detach(self, skill_name):
        skill_index = self.skill_name.index(skill_name)
        del self.skill[skill_index]
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
                if not(projectile_name.Is_Penetrate):
                    projectile_name.destroy(projectile_name.position.index(positions))
                return True
        return False
    def use_skill(self, skill_name):
        skill_index = self.skill.index(skill_name)
        if self.mp - skill_name.mp >= 0 and self.skill_cooltime[skill_index] == 0:
            skill_name.active(self)
            self.mp -= skill_name.mp
            self.skill_cooltime[skill_index] = self.skill_max_cooltime[skill_index]
        else:
            pass
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
    def __init__(self, image, All_Projectile, Is_Penetrate, Damage):
        self.image = pygame.image.load(image)
        self.position = []
        self.dx = 0
        self.dy = 0
        self.Is_Penetrate = Is_Penetrate
        self.dmg = Damage
        All_Projectile.add(self)
    def add(self, x_pos, y_pos, Dir):
        self.position.append([x_pos, y_pos, Dir])
    def destroy(self, projectile_index):
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
                self.position[position_index][1] += self.dy
            
    def draw(self, screen):
        for positions in self.position:
            x_pos = positions[0]
            y_pos = positions[1]

            screen.blit(self.image, (x_pos, y_pos))
            
class Skill():
    def __init__(self):
        pass


class t_Entity():
    def __init__(self):
        self.Entities = []
    def add(self, Entity_name):
        self.Entities.append(Entity_name)
    def destory(self, Entity_name):
        Entity_index = self.Entities.index(Entity_name)
        del self.Entities[Entity_index]
    def advance(self):
        for Entities in self.Entities:
            Entities.advance()
    def active_cooltime_tick(self):
        for Entities in self.Entities:
            Entities.active_cooltime_tick()
    def draw(self, screen):
        for Entities in self.Entities:
            Entities.draw(screen)
        
        
class t_Projectile():
    def __init__(self):
        self.Projectiles = []
    def add(self, Projectile_name):
        self.Projectiles.append(Projectile_name)
    def destory(self, Projectile_name):
        Projectile_index = self.Projectiles.index(Projectile_name)
        del self.Projectiles[Projectile_index]
    def advance(self):
        for Projectiles in self.Projectiles:
            Projectiles.advance()
    def draw(self, screen):
        for Projectiles in self.Projectiles:
            Projectiles.draw(screen)
    
    
        
