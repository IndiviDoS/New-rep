import pygame 
import random 
import sys 

# Constants 
WIDTH, HEIGHT = 400, 300 
GRID_SIZE = 20 
GRID_WIDTH = WIDTH // GRID_SIZE 
GRID_HEIGHT = HEIGHT // GRID_SIZE 
FPS = 5.25 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLACK = (0, 0, 0) 
YELLOW = (255, 255, 51) 

# Snake class 
class Snake: 
    def __init__(self): 
        self.head = [GRID_WIDTH // 2, GRID_HEIGHT // 2] 
        self.body = [[self.head[0], self.head[1]], [self.head[0] - 1, self.head[1]], [self.head[0] - 2, self.head[1]]] 
        self.direction = 'RIGHT' 

    def change_direction(self, direction): 
        if direction == 'RIGHT' and self.direction != 'LEFT': 
            self.direction = 'RIGHT' 
        elif direction == 'LEFT' and self.direction != 'RIGHT': 
            self.direction = 'LEFT' 
        elif direction == 'UP' and self.direction != 'DOWN': 
            self.direction = 'UP' 
        elif direction == 'DOWN' and self.direction != 'UP': 
            self.direction = 'DOWN' 

    def move(self): 
        if self.direction == 'RIGHT': 
            self.head[0] += 1 
        elif self.direction == 'LEFT': 
            self.head[0] -= 1 
        elif self.direction == 'UP': 
            self.head[1] -= 1 
        elif self.direction == 'DOWN': 
            self.head[1] += 1 

        self.body.insert(0, list(self.head)) 
        self.body.pop()  # Remove the last segment 

    def grow(self): 
        self.body.insert(0, list(self.head)) 

    def collide_with_wall(self): 
        if self.head[0] < 0 or self.head[0] >= GRID_WIDTH or self.head[1] < 0 or self.head[1] >= GRID_HEIGHT: 
            return True 
        return False 

    def collide_with_self(self): 
        if self.head in self.body[1:]: 
            return True 
        return False 

# Food class 
class Food: 
    def __init__(self): 
        self.position = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)] 
        self.is_food_on_screen = True 

    def spawn_food(self): 
        if not self.is_food_on_screen: 
            self.position = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)] 
            self.is_food_on_screen = True 
        return self.position 

# Weight food class 
class Weight_Food: 
    def __init__(self): 
        self.position = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)] 
        self.is_food_on_screen = True 

    def spawn_food(self): 
        if not self.is_food_on_screen: 
            self.position = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)] 
            self.is_food_on_screen = True 
        return self.position 

# Timed Food class 
class TimedFood: 
    def __init__(self, delay): 
        self.position = None 
        self.is_food_on_screen = False 
        self.delay = delay 
        self.timer = 0 

    def update(self): 
        self.timer += 1 
        if self.timer >= self.delay: 
            self.position = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)] 
            self.is_food_on_screen = True 
            self.timer = 0 

    def spawn_food(self): 
        return self.position 

# Main function 
def main(): 
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption('Snake Game') 
    clock = pygame.time.Clock() 

    snake = Snake() 
    food = Food() 
    WeightFood = Weight_Food() 
    #задержка на 8 кадров 
    timed_food = TimedFood(8) 
    apples_eaten = 0 

    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP: 
                    snake.change_direction('UP') 
                elif event.key == pygame.K_DOWN: 
                    snake.change_direction('DOWN') 
                elif event.key == pygame.K_LEFT: 
                    snake.change_direction('LEFT') 
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT') 

        snake.move() 
    
        # Check for collisions 
        if snake.collide_with_wall() or snake.collide_with_self(): 
            # Game over condition 
            pygame.quit() 
            sys.exit() 

        if snake.head == food.position: 
            snake.grow() 
            food.is_food_on_screen = False 
            apples_eaten += 1 

        if snake.head == WeightFood.position: 
            snake.grow() 
            WeightFood.is_food_on_screen = False 
            apples_eaten += 2 
        
        if snake.head == timed_food.position: 
            snake.grow() 
            timed_food.is_food_on_screen = False 
            apples_eaten += 5 

        screen.fill(BLACK) 

        for segment in snake.body: 
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) 
        
        food_position = food.spawn_food() 
        pygame.draw.rect(screen, RED, (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) 

        WeightFood_position = WeightFood.spawn_food() 
        pygame.draw.rect(screen, YELLOW, (WeightFood_position[0] * GRID_SIZE, WeightFood_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) 
        
        timed_food.update() 
        if timed_food.is_food_on_screen: 
            timed_food_position = timed_food.spawn_food() 
            pygame.draw.rect(screen, (50, 50, 50), (timed_food_position[0] * GRID_SIZE, timed_food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)) 

        # Display the number of apples eaten 
        font = pygame.font.Font(None, 36) 
        text = font.render(f'Apples eaten: {apples_eaten}', True, WHITE) 
        screen.blit(text, (10, 10)) 

        pygame.display.update() 
        clock.tick(FPS) 

if __name__ == "__main__": 
    main()