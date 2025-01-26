import pygame
from sys import exit

score = 0
deaths = 0

def displayScore():
    timeMili = pygame.time.get_ticks() - start_time
    score = timeMili//1000
    score_surface = test_font.render("score: " + str(score), False, (64,64,64))
    score_hitbox = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_hitbox)




score_total = 0
pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill("blue")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\\Pixeltype.ttf',50)
gameOver = False
start_time = 0
ground = pygame.image.load("graphics\\ground.png").convert()
backGround = pygame.image.load("graphics\\sky.png").convert()


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

# Intro Screen
player_stand = pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_hitbox = player_stand.get_rect(center = (400,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if not gameOver:
            if (event.type == pygame.KEYDOWN) and (player_hitbox.bottom == 300):
                player_gravity = -20
                print('jump')
        else:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                gameOver = False
                snail_hitbox.left = 800
                start_time = pygame.time.get_ticks()

    if not gameOver:
        
        print(score)
        screen.blit(backGround, (0,0))
        screen.blit(ground, (0,300))
        # text_surface = test_font.render('Score: '+ str(displayScore()), False, 'Green')
        # score_hitbox = text_surface.get_rect(midbottom = (400, 50))
        # screen.blit(text_surface, score_hitbox)  

        displayScore()


        snail_hitbox.left -= 6
        if snail_hitbox.right < 0 : snail_hitbox.left = 800
        screen.blit(snail_surface, (snail_hitbox))

        player_gravity += 1
        player_hitbox.y += player_gravity
        if player_hitbox.bottom >=300: player_hitbox.bottom = 300 
        screen.blit(player_surface, player_hitbox)


        if player_hitbox.colliderect(snail_hitbox):
            gameOver = True

    else: 
        start_time = pygame.time.get_ticks()
        screen.fill(('red'))
        screen.blit(player_stand,player_stand_hitbox)
        deaths += 1
        game_over_text = test_font.render("Game    Over", False, (64,64,64))
        game_over_text = pygame.transform.scale2x(game_over_text)
        game_over_rect = game_over_text.get_rect(center = (400,50))

        play_again_text = test_font.render("Press space bar to play again!", False, (64,64,64))
        play_again_rect = play_again_text.get_rect(center = (400,350))

        score_text = test_font.render("Score", False, (64,64,64))
        score_text = pygame.transform.scale2x(score_text)
        score_rect = score_text.get_rect(center = (150,150))

        numScore_text = test_font.render(str(score_total),False, (64,64,64))
        numScore_text = pygame.transform.scale2x(numScore_text)
        numScore_rect = numScore_text.get_rect(center = (150,225))

        screen.blit(play_again_text, play_again_rect)
        screen.blit(game_over_text,game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(numScore_text, numScore_rect)


            

    


        
    clock.tick(60)
    pygame.display.update()
