import os.path
import random
import time
import threading
import sys
import pygame
import pyautogui


pygame.init()

# Window view
win_width = 1600
win_height = 1200
win = pygame.display.set_mode((win_width, win_height))

# World view
world_width = 3590
world_height = 2252
world = pygame.Surface((world_width, world_height))

# Camera view
camera = pygame.Rect(0, 0, win_width, win_height)

# Background
bg = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Background', 'intersection.png'))


world.blit(bg,(0,0))

# Mouse movement
dragging = False
prev_mouse_pos = (0, 0)

vehicleTypes = {0:'car', 1:'bus', 2:'truck', 3:'bike'}
directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'}

#Start coordinates
rightCordStart = [[1590,830],[1590,876],[1590,496],[1590,1590,549],[1590,235],[1590,278]]

class Vehicle(pygame.sprite.Sprite):
    def __int__(self, lane,):
        pygame.sprite.Sprite.__init__(self)


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    camera.move_ip(5, 0)  # Move the camera 5 pixels to the right
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    prev_mouse_pos = pygame.mouse.get_pos()
                    print(f'World coordinate: {pygame.mouse.get_pos()}')
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
        if dragging:
            mouse_pos = pygame.mouse.get_pos()
            dx, dy = prev_mouse_pos[0] - mouse_pos[0] , prev_mouse_pos[1] - mouse_pos[1]
            camera.move_ip(dx,dy)
            camera.clamp_ip(world.get_rect())
            prev_mouse_pos = mouse_pos

        win.blit(world.subsurface(camera), (0, 0))
        pygame.display.flip()
