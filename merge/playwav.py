import pygame
pygame.mixer.init()

def play(index):
	if index == 0:
		sound = pygame.mixer.Sound('wate.wav')
		sound.play()
	elif index == 1:
		sound = pygame.mixer.Sound('thund.wav')
		sound.play()
	