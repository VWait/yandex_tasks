import pygame


def change_point(point, k, c):
    return tuple(map(lambda x: x * k + c, list(point)))


def change_pol(points, k, center):
    k = [k] * len(points)
    c = [center] * len(points)
    return list(map(change_point, points, k, c))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    running = True

    center = width / 2

    with open('points.txt', 'r') as file:
        points = [tuple(map(float, i.replace(',', '.').split(';')))
                  for i in file.read()[1:-1].split('), (')]
        points = list(map(lambda x: (x[0], -x[1]), points))
        print(points)
    k = 15
    v = 1.2
    points_state = points
    points = change_pol(points, k, center)

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    k *= v
                    points = change_pol(points_state, k, center)
                if event.button == 5:
                    k /= v
                    points = change_pol(points_state, k, center)
        pygame.draw.polygon(screen, 'white', points, width=2)
        pygame.display.flip()

    pygame.quit()
