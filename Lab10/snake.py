import pygame
import random
import psycopg2
from config import *

def Score_snake():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS Score_snake (user_name VARCHAR(64) NOT NULL PRIMARY KEY, user_score BIGINT NOT NULL);"
            )
            print("Table created")

    except Exception as ex:
        print("[INFO] Error while creating table:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

def insert_user_score(user_name, user_score):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Score_snake (user_name, user_score)
                VALUES (%s, %s)
            """, (user_name, user_score))
            
        print("Score inserted successfully.")

    except Exception as ex:
        print("[INFO] Error while inserting score:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

# Call Score_snake function to create table
Score_snake()

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
extra_food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
food_spawn = True
extra_food_spawn = True

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
dir = RIGHT
score = 0
level = 1
snake_speed = 15
game_over = False
paused = False

clock = pygame.time.Clock()

username = ""

while not username:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    username = input("Enter your username: ")

# Get user input for username before starting the game loop

def move_snake():
    global dir, snake_pos, snake_body, food_pos, extra_food_pos, score, level, snake_speed, game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != DOWN:
                dir = UP
            elif event.key == pygame.K_DOWN and dir != UP:
                dir = DOWN
            elif event.key == pygame.K_LEFT and dir != RIGHT:
                dir = LEFT
            elif event.key == pygame.K_RIGHT and dir != LEFT:
                dir = RIGHT
            elif event.key == pygame.K_p:
                paused = not paused

    if not paused:
        if dir == UP:
            snake_pos[1] -= 10
        elif dir == DOWN:
            snake_pos[1] += 10
        elif dir == LEFT:
            snake_pos[0] -= 10
        elif dir == RIGHT:
            snake_pos[0] += 10

        if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
            game_over = True

        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        elif snake_pos[0] == extra_food_pos[0] and snake_pos[1] == extra_food_pos[1]:
            score += 5
            extra_food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
            food_spawn = True

        if not extra_food_spawn:
            extra_food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
            extra_food_spawn = True

        snake_body.insert(0, list(snake_pos))

def draw_screen():
    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    pygame.draw.rect(screen, GREEN, pygame.Rect(extra_food_pos[0], extra_food_pos[1], 10, 10))

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score) + "   Level: " + str(level), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

while not game_over:
    move_snake()
    draw_screen()
    clock.tick(snake_speed)

# Close the database connection
conn.close()
pygame.quit()
