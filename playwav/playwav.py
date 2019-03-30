import pygame
pygame.mixer.init()

sound = pygame.mixer.Sound('demo.wav')
while True:
	sound.play()