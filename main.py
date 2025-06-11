import pygame
import random
import sys

WIDTH, HEIGHT = 640, 480
PLAYER_SPEED = 5
BULLET_SPEED = -7
ENEMY_SPEED = 2
SPAWN_EVENT = pygame.USEREVENT + 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 100, 255), (15, 15), 15)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        return bullet


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((200, 0, 0))
        x = random.randint(15, WIDTH - 15)
        self.rect = self.image.get_rect(midbottom=(x, 0))
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball Blaster")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    player = Player()
    all_sprites = pygame.sprite.Group(player)
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    score = 0
    level = 1
    lives = 3
    spawn_delay = 1000  # milliseconds
    pygame.time.set_timer(SPAWN_EVENT, spawn_delay)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_EVENT:
                enemy = Enemy()
                enemies.add(enemy)
                all_sprites.add(enemy)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    bullets.add(bullet)
                    all_sprites.add(bullet)

        keys = pygame.key.get_pressed()
        player.update(keys)
        bullets.update()
        enemies.update()

        # bullet-enemy collisions
        if collisions := pygame.sprite.groupcollide(bullets, enemies, True, True):
            score += len(collisions)
            if score % 10 == 0:
                level += 1
                spawn_delay = max(200, spawn_delay - 50)
                pygame.time.set_timer(SPAWN_EVENT, spawn_delay)
                for e in enemies:
                    e.speed += 0.5

        # enemy-player collisions
        if pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
            if lives <= 0:
                running = False

        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        info = font.render(f"Score: {score}  Level: {level}  Lives: {lives}", True, (255, 255, 255))
        screen.blit(info, (10, 10))
        pygame.display.flip()
        clock.tick(60)

    # game over screen
    over_text = font.render(f"Game Over! Final score: {score}", True, (255, 255, 255))
    rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(over_text, rect)
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
