import pygame

FPS = 60
white = (255, 255, 255)


# game initialization
pygame.init()
clock pyhon.time.Clock
screan = pygame.display.set_mode((500, 600)) #set screan size

running = True

while running:
	clock.tick(FPS) # limit loop times FPS

	#Get input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#Update

	#display
	screan.fill((white)) # Adjust color use rgb
	python.display.update()
pygame.quit()
