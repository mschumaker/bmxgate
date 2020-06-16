import pygame
pygame.mixer.init()
shortTone = pygame.mixer.Sound("632_2250ms.wav");
shortTone.play()
while pygame.mixer.music.get_busy() == True:
    continue