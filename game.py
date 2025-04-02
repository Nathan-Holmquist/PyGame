# My best score is 104
# Best score ever Francis - 107

import pygame
from sys import exit
import os
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()   

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))

        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.05)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        # jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_1,fly_2] 
            if total_enemies > 10: y_pos = 170
            else: y_pos = 210
            
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= enemy_speed
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def displayScore():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = test_font.render(f'Score:  {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

    return current_time

def enemyMovement(enemy_List):
    if enemy_List:
        for enemy_rect in enemy_List:
            if enemy_rect.bottom == 300:
                screen.blit(snail_surf, enemy_rect)
            else:
                screen.blit(fly_surf, enemy_rect)    
        enemy_List = [enemy for enemy in enemy_List if enemy.x > -100]
    return enemy_List

def getCollideSprites():
    if pygame.sprite.spritecollide(player.sprite, enemy_group, False):
        enemy_group.empty()
        return True
    else:
        return False 

def getPlayerAnimation():
    global player_surf, player_index

    if player_hitbox.bottom < 300:
        player_surf = player_jump
        # jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
        # floor    




base_path = os.path.dirname(os.path.abspath(__file__))
score = 0
highScore = 0
highScoreHappened = True
start_time = 0
total_enemies = 0
enemy_speed = 5
pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill("blue")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
gameOver = True
ground = pygame.image.load("graphics/ground.png").convert()
backGround = pygame.image.load("graphics/sky.png").convert()

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.05)
bg_music.play(loops = -1)

player_gravity = 0
player = pygame.sprite.GroupSingle()
player.add(Player())

enemy_group = pygame.sprite.Group()

enemy_hitbox_list = []
time_tick = 0 # Used to increase enemy speed 
firstEnemy = True # True if this is the first enemy in the game


player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_hitbox = player_surf.get_rect(midbottom = (80,300 + player_gravity))

# Intro Screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_hitbox = player_stand.get_rect(center = (400,200))


    

while True: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if not gameOver: #if game is running
            time_tick += 0.00001 # Only used to increase enemy speed

            if (event.type == enemy_timer):
                enemy_group.add(Enemy(choice(['fly','snail','snail'])))
                total_enemies += 1


        else:   # if game is not running
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                start_time = pygame.time.get_ticks()
                gameOver = False
                enemy_speed = 5
                time_tick = 0
                highScoreHappened = False
                total_enemies = 0

                # Timer's
                enemy_timer = pygame.USEREVENT + 1
                pygame.time.set_timer(enemy_timer, 1500)

                snail_animation_timer = pygame.USEREVENT + 2
                pygame.time.set_timer(snail_animation_timer, 350)

                fly_animation_timer = pygame.USEREVENT + 3
                pygame.time.set_timer(fly_animation_timer, 200)

                # If the user starts a new game, an enemy should spawn instantly
                enemy_group.add(Enemy(choice(['fly','snail','snail'])))
                total_enemies += 1




    if not gameOver: 
        enemy_speed += time_tick

        screen.blit(backGround, (0,0))
        screen.blit(ground, (0,300))

        score = displayScore()
        if score > highScore:
            highScore = score
            highScoreHappened = True

 


        player.draw(screen)
        player.update()

        enemy_group.draw(screen)
        enemy_group.update()


        # Enemy Movement
        enemy_hitbox_list =  enemyMovement(enemy_hitbox_list)


        gameOver = getCollideSprites()

    else: 
        
        # Game Over
        firstEnemy = True

        game_over_text = test_font.render("Game    Over", False, (64,64,64))
        game_over_text = pygame.transform.scale2x(game_over_text)
        game_over_rect = game_over_text.get_rect(center = (400,50))

        play_again_text = test_font.render("Press space bar to play again!", False, (64,64,64))
        play_again_rect = play_again_text.get_rect(center = (400,350))

        score_text = test_font.render("Score", False, (64,64,64))
        score_text = pygame.transform.scale2x(score_text)
        score_rect = score_text.get_rect(center = (150,150))

        high_score_text = test_font.render("High Score!", False, (64,64,64))
        # high_score_text = pygame.transform.scale2x(high_score_text)
        high_score_rect = high_score_text.get_rect(center = (150,150))

        score_num = test_font.render(f'{score}', False, (0,0,0))
        score_num = pygame.transform.scale2x(score_num)
        score_num_rect = score_num.get_rect(center = (150,225))

        # Opening Screen
        
        play_again_title = test_font.render("Press space bar to play!", True, ('lightgreen'))
        play_again_title_rect = play_again_title.get_rect(center = (400,350))

        game_title = test_font.render("Super       Game", False, ('lightgreen'))
        game_title = pygame.transform.scale2x(game_title)
        game_hitbox = game_title.get_rect(center = (390,125))

        game_dev = test_font.render("By: Nathan   Holmquist", False, ('lightgreen'))
        game_dev_hitbox = game_dev.get_rect(center = (400,300))

        title_player = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        title_player = pygame.transform.scale2x(title_player)
        title_player_hitbox = title_player.get_rect(center = (400,200))

        title_fly = pygame.image.load('graphics/Fly/fly1.png').convert_alpha()
        title_fly = pygame.transform.scale2x(title_fly)
        title_fly_hitbox = title_fly.get_rect(center = (200,200))

        title_snail = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
        title_snail = pygame.transform.scale2x(title_snail)
        title_snail_hitbox = title_snail.get_rect(center = (600,200))


        if score != 0:
            screen.fill('red')
            screen.blit(player_stand,player_stand_hitbox)
            if highScoreHappened:
                screen.blit(high_score_text, high_score_rect)
            else:
                screen.blit(score_text, score_rect)
            
            screen.blit(game_over_text,game_over_rect)
            screen.blit(score_num, score_num_rect)
            
            screen.blit(play_again_text, play_again_rect)
            enemy_hitbox_list.clear()

        else:
            screen.fill((111,196,249))
            screen.blit(game_title, game_hitbox)
            screen.blit(game_dev, game_dev_hitbox)
            screen.blit(title_player, title_player_hitbox)
            screen.blit(title_fly, title_fly_hitbox)
            screen.blit(title_snail, title_snail_hitbox)
            screen.blit(play_again_title, play_again_title_rect)
 

        
        
        


            

    


        
    clock.tick(60)
    pygame.display.update()
