import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill("blue")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\\Pixeltype.ttf',50)

ground = pygame.image.load("graphics\\ground.png").convert()
backGround = pygame.image.load("graphics\\sky.png").convert()
text_surface = test_font.render('My game', False, 'Green')
color_surface = pygame.Surface((100,100))
color_surface.fill("red")






# PLAYER CORDS
player_x_pos = 0
player_y_pos = 0


snail_surface = pygame.image.load("graphics\\snail\\snail1.png").convert_alpha()
snail_hitbox = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load("graphics\\Player\\player_stand.png").convert_alpha()
player_hitbox = player_surface.get_rect(midbottom = (80,300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(backGround, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(text_surface, (300,50))
    screen.blit(snail_surface, (snail_hitbox))
    screen.blit(player_surface, player_hitbox)
    screen.blit(color_surface,(200,100))



    snail_hitbox.left -= 4
    if snail_hitbox.right < 0 : snail_hitbox.left = 800

    # if player_hitbox.colliderect(snail_hitbox):
    #     color_surface.fill('green')
    # else:
    #     color_surface.fill('red')

    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    mouse_pos_text = test_font.render(str(mouse_pos), False, 'Green')
    screen.blit(mouse_pos_text, (300,100))
    
    if player_hitbox.collidepoint(mouse_pos):
        color_surface.fill('green')
    else:
        color_surface.fill('red')
        
    clock.tick(60)
    pygame.display.update()
