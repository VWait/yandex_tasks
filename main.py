import pygame
from math import sin, cos, radians


def create_point(degree, r, x, y):
    return cos(radians(degree)) * r + x, \
           sin(radians(degree)) * r + y


def draw_triangle(degree, r, center):
    center_x = center[0]
    center_y = center[1]
    point_1 = create_point(degree, r, center_x, center_y)
    point_2 = create_point(degree + 30, r, center_x, center_y)
    pygame.draw.polygon(screen, 'white', [center, point_1, point_2], 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()

    center = (100, 100)
    now_pos = 75
    h = 70
    v = 50

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    v += 50
                elif event.button == 3:
                    v -= 50

        screen.fill((0, 0, 0))

        draw_triangle(now_pos, h, center)
        draw_triangle(now_pos + 120, h, center)
        draw_triangle(now_pos + 240, h, center)
        pygame.draw.circle(screen, 'white', center, 10)
        now_pos += v * clock.tick() / 1000

        pygame.display.flip()

    pygame.quit()
