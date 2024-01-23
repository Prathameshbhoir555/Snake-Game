import pygame,sys,random
from pygame.math import Vector2


#class for snake and GUI images import
#dfidsfdjavnda

class SNAKE:
	def __init__(snake):
		snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		snake.direction = Vector2(0,0)
		snake.new_block = False

		snake.head_up = pygame.image.load('C:\\Users\\H\\snake game graphics\\snake head up.png').convert_alpha()
		snake.head_down = pygame.image.load('C:\\Users\\H\\snake game graphics\\snake head down.png').convert_alpha()
		snake.head_right = pygame.image.load('C:\\Users\\H\\snake game graphics\\snake head right.png').convert_alpha()
		snake.head_left = pygame.image.load('C:\\Users\\H\\snake game graphics\\snake head left.png').convert_alpha()
		
		snake.tail_up = pygame.image.load('C:\\Users\\H\\snake game graphics\\tail up.png').convert_alpha()
		snake.tail_down = pygame.image.load('C:\\Users\\H\\snake game graphics\\tail down.png').convert_alpha()
		snake.tail_right = pygame.image.load('C:\\Users\\H\\snake game graphics\\tail right.png').convert_alpha()
		snake.tail_left = pygame.image.load('C:\\Users\\H\\snake game graphics\\tail left.png').convert_alpha()

		snake.vertical_body = pygame.image.load('C:\\Users\\H\\snake game graphics\\vertical body.png').convert_alpha()
		snake.horizontal_body = pygame.image.load('C:\\Users\\H\\snake game graphics\\horizontal body.png').convert_alpha()

		snake.body_tail_right = pygame.image.load('C:\\Users\\H\\snake game graphics\\body tail right.png').convert_alpha()
		snake.body_tail_left = pygame.image.load('C:\\Users\\H\\snake game graphics\\body tail left.png').convert_alpha()
		snake.body_body_right = pygame.image.load('C:\\Users\\H\\snake game graphics\\body right.png').convert_alpha()
		snake.body_body_left = pygame.image.load('C:\\Users\\H\\snake game graphics\\body left.png').convert_alpha()
		snake.sound_crunch = pygame.mixer.Sound('C:\\Users\\H\\snake game graphics\\crunch.wav')

	def snake_draw(self):
		self.update_HeadGraphics()
		self.update_TailGraphics()

		for index,block in enumerate(self.body):
			x_position = int(block.x * cell_size)
			y_position = int(block.y * cell_size)
			rectangle_block = pygame.Rect(x_position,y_position,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,rectangle_block)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,rectangle_block)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.vertical_body,rectangle_block)
				elif previous_block.y == next_block.y:
					screen.blit(self.horizontal_body,rectangle_block)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tail_left,rectangle_block)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_body_left,rectangle_block)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tail_right,rectangle_block)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_body_right,rectangle_block)
	
	#update of GUI when its head turns at any direction 
						
	def update_HeadGraphics(self):

		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down
	
	#update of GUI when its tail turns at any direction
		
	def update_TailGraphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def MoveSnake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

	#sound for fruit
		
	def play_sound_crunch(self):
		self.sound_crunch.play()

	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)

# For Fruit
		
class FRUIT:
	def __init__(self):
		self.randomize()         

	def fruit_draw(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(apple,fruit_rect)
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

	def randomize(self):                              #randomise the locations of fruit
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)

class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()

	def update(self):
		self.snake.MoveSnake()
		self.check_collision()
		self.CheckFail()

	def draw_elements(self):
		self.draw_grass()
		self.fruit.fruit_draw()
		self.snake.snake_draw()
		self.draw_score()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_sound_crunch()

		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def CheckFail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.GameOver()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.GameOver()
		
	def GameOver(self):
		self.snake.reset()

	def draw_grass(self):
		grass_color = (167,209,61)
		for row in range(cell_number):
			if row % 2 == 0: 
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rectangle = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rectangle)
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rectangle = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rectangle)			

	def draw_score(self):
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		pygame.draw.rect(screen,(167,209,61),bg_rect)
		screen.blit(score_surface,score_rect)
		screen.blit(apple,apple_rect)
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('C:\\Users\\H\\snake game graphics\\apple.png').convert_alpha()
game_font = pygame.font.Font('C:\\Users\\H\\snake game graphics\\PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

#User Input Directions

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	screen.fill((175,215,70))
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)


	




