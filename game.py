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

# Indicator for collision
color_surface = pygame.Surface((100,100))
color_surface.fill("red")







# PLAYER CORDS
player_x_pos = 0
player_y_pos = 0
player_gravity = 0

hitbox_indicator = color_surface.get_rect(topright = (800,0))

snail_surface = pygame.image.load("graphics\\snail\\snail1.png").convert_alpha()
snail_hitbox = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load("graphics\\Player\\player_stand.png").convert_alpha()
player_hitbox = player_surface.get_rect(midbottom = (80,300 + player_gravity))

score_hitbox = text_surface.get_rect(midbottom = (400, 50))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if (event.type == pygame.KEYDOWN) and (player_hitbox.bottom == 300):
            player_gravity = -20
            print('jump')


    
    screen.blit(backGround, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(text_surface, score_hitbox)  
    screen.blit(color_surface,hitbox_indicator)



    snail_hitbox.left -= 6
    if snail_hitbox.right < 0 : snail_hitbox.left = 800
    screen.blit(snail_surface, (snail_hitbox))

    player_gravity += 1
    player_hitbox.y += player_gravity
    if player_hitbox.bottom >=300: player_hitbox.bottom = 300 
    screen.blit(player_surface, player_hitbox)


    if player_hitbox.colliderect(snail_hitbox):
        color_surface.fill('green')
        pygame.quit()
        exit()
    else:
        color_surface.fill('red')

    


        
    clock.tick(60)
    pygame.display.update()
