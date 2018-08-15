import pygame
import sys
import VirusNode
from pygame.locals import *
pygame.init()
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (255, 205, 255)
bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()

bac_num = 5
doc_num = 1
split_time = 500
done = False

def process_events():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


def main():

    bacteria.add(VirusNode((random.rantint(50, width-50))))
    while not done:
        clock.tick(60)
        process_events()
        screen.fill(color)
        doctors.draw(screen)
        bacteria.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()