# Entity
Entity는 ability에서 발사체를 제외한 모든 것을 뜻합니다

# Entity method

- attatch(스킬 이름)

Entity에서 특정 skill을 부여합니다

Skill은 먼저 부여받은 순으로 append됩니다

- detach(스킬 이름)

Entity에서 특정 skill을 부여 해제합니다

- collide_entity(Entity 이름)

특정 Entity와 충돌하였는지를 판정하여 boolean 형식으로 반환합니다

- collide_projectile(Projectile 이름)

특정 projectile과 충돌하였는지를 판정하여 이를 boolean 형식으로 반환합니다

- use_skill(skill 번호)

Skill 번호의 스킬을 실행합니다

- draw_entity(상위 윈도우)

상위 윈도우에 entity를 그립니다


# Entity variables

- self.max_hp

Entity의 최대 채력

- self.max_mp

Entity의 최대 mp

- self.x

Entity의 x좌표

- self.y

Entity의 y좌표
