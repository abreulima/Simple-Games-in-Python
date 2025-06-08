import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
x, y = 200, 150
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 30, 30))
    pygame.display.flip()
    clock.tick(60)

