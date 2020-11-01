import pygame
import ability

class a_spiral(ability.Skill):
    def __init__(self, All_Projectile):
        self.mp = 10
        self.cooltime = 600
        self.name = "나선환"
        self.description = "마나 {}을 소모하여 플레이어가 보는 방향으로 나선환을 발사합니다".format(self.mp)
        self.spiral = ability.Projectile('spiral.png', All_Projectile)
    def active(self, caster):
        self.spiral.add(caster.x + caster.dir * 5, caster.y, caster.dir)
        self.spiral.dx = 6
