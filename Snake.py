import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
        def __init__(self):
                self.body = [Vector2(5, 10), Vector2(6,10), Vector2(7,10)]
                self.direction = Vector2(1,0)
                self.new_block = False

        def draw_snake(self):
                for block in self.body:
                        x_pos = block.x*cell_size
                        y_pos = block.y*cell_size
                        block_rect = pygame.Rect(x_pos, y_pos, cell_size,cell_size)
                        
                        pygame.draw.rect(screen, (183,111,122), block_rect)
        def move_snake(self):

                if self.new_block == True:
                
                        body_copy = self.body[:] #copio solo las primeras celdas meno la ultima
                        body_copy.insert(0,body_copy[0] + self.direction) #inserto una nueva celda al principio
                        self.body = body_copy[:] #La asigno com la original
                        self.new_block = False #Cuando impacta volvemos a false

                else:
                        body_copy = self.body[:-1]
                
                        body_copy.insert(0,body_copy[0] + self.direction) #inserto una nueva celda al principio
                        self.body = body_copy[:] #La asigno com la original
        
        def add_block(self):
                self.new_block = True
        
        


class FRUIT:
        def __init__(self):
                self.randomize()
        def draw_fruit(self):
                fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size,cell_size,cell_size)
                pygame.draw.rect(screen,(226,46,14),fruit_rect)
        def randomize(self):
                self.x = random.randint(0,cell_number -1)
                self.y = random.randint(0,cell_number -1)
                self.pos = Vector2(self.x, self.y)
        


class MAIN:
        def __init__(self):
                self.snake = SNAKE()
                self.fruit = FRUIT()

        def update(self):
                self.snake.move_snake()
                self.check_collision()
        
        def draw_elements(self):
                self.fruit.draw_fruit()
                self.snake.draw_snake()
        
        def check_collision(self):
                if self.fruit.pos == self.snake.body[0]:#coincide la cabeza con la posicion de la fruta
                        self.fruit.randomize() #reposicionamiento de la fruta
                        self.snake.add_block()
                        

pygame.init()
cell_size= 40
cell_number=20
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock = pygame.time.Clock()



SCREEN_UPDATE = pygame.USEREVENT # los eventos se escriben en mayuscula
pygame.time.set_timer(SCREEN_UPDATE, 200)

main_game = MAIN()

while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == SCREEN_UPDATE:
                        main_game.update()
                
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                main_game.snake.direction = Vector2(0, -1)
                        if event.key == pygame.K_DOWN:
                                main_game.snake.direction = Vector2(0, 1)
                        if event.key == pygame.K_LEFT:
                                main_game.snake.direction = Vector2(-1, 0)
                        if event.key == pygame.K_RIGHT:
                                main_game.snake.direction = Vector2(1, 0)

        screen.fill((175,215,70))
        main_game.draw_elements()
        
        pygame.display.update()
        clock.tick(60)