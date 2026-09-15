import pygame
import random
import sys
import cv2

# Initialize Pygame
pygame.init()

# Set up game window
WIDTH, HEIGHT = 700, 500
gamewindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Auto-Firing Tank Game with Video Background")

# Load Video with OpenCV
video = cv2.VideoCapture(r"D:\rohit\4th month\galaxy.mp4")  # apna video path
video = cv2.VideoCapture(r"D:\rohit\4th month\galaxy.mp4")  # apna video path
if not video.isOpened():
    print("Error: Video file not found!")
    sys.exit()

# Tank Image
tank_img = pygame.image.load(r"D:\rohit\4th month\tank.jpg")
tank_img = pygame.transform.scale(tank_img, (60, 60))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Tank properties
tank_x = WIDTH // 2
tank_y = HEIGHT - 70
tank_speed = 5

# Bullets
bullets = []
bullet_speed = 10
bullet_timer = 0
bullet_delay = 5

# Enemies
enemy_img = pygame.Surface((40, 40))
enemy_img.fill(RED)
enemies = []
enemy_speed = 2
spawn_delay = 40
enemy_timer = 0

# Enemy Bullets
enemy_bullets = []
enemy_bullet_speed = 6
enemy_bullet_delay = 60
enemy_bullet_timer = 0

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Game Over Flag
game_over = False

# Main Game Loop
while True:
    clock.tick(FPS)

    # ---- BACKGROUND VIDEO ----
    ret, frame = video.read()
    if not ret: 
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = video.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    gamewindow.blit(frame_surface, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            video.release()
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and tank_x > 0:
            tank_x -= tank_speed
        if keys[pygame.K_RIGHT] and tank_x < WIDTH - 60:
            tank_x += tank_speed

        # Auto-fire bullets
        bullet_timer += 1
        if bullet_timer >= bullet_delay:
            bullets.append([tank_x + 25, tank_y])
            bullet_timer = 0

        for bullet in bullets:
            bullet[1] -= bullet_speed
        bullets = [b for b in bullets if b[1] > 0]

        enemy_timer += 1
        if enemy_timer >= spawn_delay:
            enemies.append([random.randint(0, WIDTH - 40), -40])
            enemy_timer = 0

        for enemy in enemies:
            enemy[1] += enemy_speed

        enemy_bullet_timer += 1
        if enemy_bullet_timer >= enemy_bullet_delay:
            for enemy in enemies:
                enemy_bullets.append([enemy[0] + 20, enemy[1] + 40])
            enemy_bullet_timer = 0

        for e_bullet in enemy_bullets:
            e_bullet[1] += enemy_bullet_speed
        enemy_bullets = [b for b in enemy_bullets if b[1] < HEIGHT]

        # Collision Detection
        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 10)
            for enemy in enemies:
                enemy_rect = pygame.Rect(enemy[0], enemy[1], 40, 40)
                if bullet_rect.colliderect(enemy_rect):
                    try:
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        score += 1
                    except:
                        pass

        for enemy in enemies:
            if enemy[1] + 40 > tank_y and tank_x < enemy[0] + 40 and tank_x + 60 > enemy[0]:
                game_over = True

        tank_rect = pygame.Rect(tank_x, tank_y, 60, 60)
        for e_bullet in enemy_bullets:
            e_bullet_rect = pygame.Rect(e_bullet[0], e_bullet[1], 5, 10)
            if tank_rect.colliderect(e_bullet_rect):
                game_over = True

        # Draw Tank
        gamewindow.blit(tank_img, (tank_x, tank_y))

        # Draw Tank Bullets
        for bullet in bullets:
            pygame.draw.rect(gamewindow, WHITE, (bullet[0], bullet[1], 5, 10))

        # Draw Enemies
        for enemy in enemies:
            gamewindow.blit(enemy_img, (enemy[0], enemy[1]))

        # Draw Enemy Bullets
        for e_bullet in enemy_bullets:
            pygame.draw.rect(gamewindow, BLACK, (e_bullet[0], e_bullet[1], 5, 10))

        # Draw Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        gamewindow.blit(score_text, (10, 10))

    else:
        over_text = font.render("GAME OVER - Press R to Restart", True, RED)
        gamewindow.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            bullets = []
            enemies = []
            enemy_bullets = []
            tank_x = WIDTH // 2
            score = 0
            game_over = False

    pygame.display.update()