import pygame
import random
import time
#initialize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#bg image
bg_image = pygame.image.load("backround.png")

#title and icon/logo
pygame.display.set_caption("Aero Tremors")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

#player attributes
playerImage = pygame.image.load("player1.png")
player_x = 400
player_y = 550
player_x_speed = 0
player_y_speed = 0

#enemy attributes
enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 769)
enemy_y = 20
enemy_x_speed = 0.5
enemy_y_speed = 75

#bullet
bullet = pygame.image.load("bullet1.png")
bullet_x = 0
bullet_y = 550
bullet_x_speed = 0
bullet_y_speed = 1

# fire - bullet is shot and visible(in motion)
# ready - you cant see the bullet
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImage, (x,y))

def enemy(x,y):
    screen.blit(enemyImage, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 4, y + 5))

# game loop
running = True 
while running:
    # RBG --> (RED, GREEN, BLUE)
    screen.fill((128,128,128))

    #drawing bg image
    screen.blit(bg_image,((0,0)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if a key is pressed check whether it is left arrow of right arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_speed = -1
            if event.key == pygame.K_RIGHT:
                player_x_speed = 1 
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(player_x, player_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_speed = 0

    player_x += player_x_speed
    enemy_x += enemy_x_speed
    # Check if bullet is fired
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_speed

    if player_x <= 0:
        player_x = 0
    if player_x >= 768:
        player_x = 768

    if enemy_x <= 0:
        enemy_x = 0
        enemy_x_speed = -enemy_x_speed
        enemy_y += enemy_y_speed
    if enemy_x >= 768:
        enemy_x = 768
        enemy_x_speed = -enemy_x_speed
        enemy_y += enemy_y_speed

    #bullet movement    
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_speed

    #player and enemy image drawn on the screen(Surface)
        
    player(player_x, player_y)  
    enemy(enemy_x, enemy_y)
    

    pygame.display.flip()    