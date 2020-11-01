import pygame
import random
import ability

class teleport(ability.Skill):
    def __init__(self, All_Projectile):
        self.mp = 10
        self.cooltime = 900
        self.name = "텔레포트"
        self.description = "플레이어를 랜덤한 위치로 텔레포트 시키고, 플레이어가 텔레포트 되기 전의 자리에 나선환을 소환합니다"
        self.spiral = ability.Projectile('spiral.png', All_Projectile)
    def active(self, caster):
        self.spiral.add(caster.x + caster.dir * 5, caster.y, caster.dir * (random.randrange(-2, 1) + 1))
        self.spiral.dx = 6
        caster.goto(random.randrange(0, 500), caster.y)
