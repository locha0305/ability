import pygame
import ability


class slash(ability.Skill):
    def __init__(self, All_Entity):
        self.mp = 0
        self.cooltime = 600
        self.name = "질풍참"
        self.description = "플레이어가 바라보는 방향으로 검을 가르며 플레이어가 지나간 경로의 적들에게 50의 데미지를 줍니다"
        self.All_Entity = All_Entity
    def active(self, caster):
        start_x = caster.x
        caster.goto(caster.x + 50 * caster.dir, caster.y)
        end_x = caster.x
        for Entity in self.All_Entity.Entities:
            if caster.dir == 1:
                if Entity.x >= start_x and Entity.x < end_x and Entity != caster:
                    Entity.hp -= 50
                else:
                    pass
            else:
                if Entity.x < start_x and Entity.x >= end_x and Entity != caster:
                    Entity.hp -= 50
                else:
                    pass
