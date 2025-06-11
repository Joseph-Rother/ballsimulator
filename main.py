import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Ball Simulator")

    clock = pygame.time.Clock()
    ball_pos = [320, 240]
    ball_vel = [2, 2]
    ball_radius = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update ball position
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # bounce off edges
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > 640:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > 480:
            ball_vel[1] = -ball_vel[1]

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
