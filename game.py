import pygame

screen = pygame.display.set_mode((550,400))
screen.fill("blue")
clock = pygame.time.Clock()

ground = pygame.image.load("graphics\\darkGrass.jpg")
backGround = pygame.image.load("graphics\\Backgrounds\\niceBackground.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground, (0,0))
    screen.blit(backGround, (0,0))

    clock.tick(60)
    pygame.display.update()
