import pygame
import random
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_SIZE = 10
FOOD_SIZE = 10
SPEED = 10
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
def draw_text(text, color, x, y):
    font = pygame.font.SysFont("arial", 25)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def draw_objects(snake, food):
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, [x, y, SNAKE_SIZE, SNAKE_SIZE])
    pygame.draw.rect(screen, RED, [food[0], food[1], FOOD_SIZE, FOOD_SIZE])
def update_game(snake, food):
    direction = get_direction()
    head_x = snake[0][0] + direction[0] * SNAKE_SIZE
    head_y = snake[0][1] + direction[1] * SNAKE_SIZE
    snake.insert(0, (head_x, head_y))
    if head_x == food[0] and head_y == food[1]:
        food = generate_food()
        score = len(snake) - 3
        if score > get_high_score():
            save_high_score(score)
    else:
        snake.pop()
    if is_collision(snake):
        game_over()
    return snake, food
def get_direction():
    direction = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
    return direction
def generate_food():
    food = (0, 0)
    food_x = random.randint(0, SCREEN_WIDTH // FOOD_SIZE - 1) * FOOD_SIZE
    food_y = random.randint(0, SCREEN_HEIGHT // FOOD_SIZE - 1) * FOOD_SIZE
    food = (food_x, food_y)
    return food
def is_collision(snake):
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        return True
    for x, y in snake[1:]:
        if head_x == x and head_y == y:
            return True
        return False
def game_over():
    draw_text("Game Over", WHITE, SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25)
    draw_text(f"Score: {len(snake) - 3}", WHITE, SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 2 + 25)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()
def get_high_score():
    high_score = 0
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
    return high_score
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))
snake = [(300, 200), (290, 200), (280, 200)]
food = generate_food()
while True:
    snake, food = update_game(snake, food)
    screen.fill(BLACK)
    draw_objects(snake, food)
    draw_text(f"Score: {len(snake) - 3}", WHITE, 10, 10)
    draw_text(f"High Score: {get_high_score()}", WHITE, SCREEN_WIDTH - 100, 10)
pygame.display.update()
clock.tick(SPEED)