import pygame, sys
from os import walk

# Pygame setup
pygame.init()

screen_width = 1440
screen_height = 1000


clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	


	pygame.display.update()
	clock.tick(60)