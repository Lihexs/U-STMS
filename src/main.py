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

# load all the images
bike_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'bike.png'))
bike_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'bike.png'))
bike_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'bike.png'))
bike_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'bike.png'))


world.blit(bg,(0,0))

bus_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'bus.png'))
bus_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'bus.png'))
bus_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'bus.png'))
bus_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'bus.png'))

car_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'car.png'))
car_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'car.png'))
car_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'car.png'))
car_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'car.png'))

truck_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'truck.png'))
truck_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'truck.png'))
truck_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'truck.png'))
truck_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'truck.png'))

speed = 10

# create a move function the given a vehicle and a direction it will move the vehicle in that direction
# create a function that will create a vehicle and add it to the list of vehicles
def move(vehicle, direction):
    if direction == 'right':
        vehicle.x += speed
    elif direction == 'down':
        vehicle.y += speed
    elif direction == 'left':
        vehicle.x -= speed
    elif direction == 'up':
        vehicle.y -= speed



world.blit(bg, (0, 0))

# Mouse movement
dragging = False
prev_mouse_pos = (0, 0)

vehicle_types = ['bike', 'bus', 'car', 'truck']
direction_dict = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}

# create a function that creates a new vehicle pygame object
def create_vehicle(vehicle_type, direction, position):
    if vehicle_type == 'bike':
        if direction == 'right':
            world.blit(bike_right, position)
        elif direction == 'down':
            world.blit(bike_down, position)
        elif direction == 'left':
            world.blit(bike_left, position)
        elif direction == 'up':
            world.blit(bike_up, position)
    elif vehicle_type == 'bus':
        if direction == 'right':
            world.blit(bus_right, position)
        elif direction == 'down':
            world.blit(bus_down, position)
        elif direction == 'left':
            world.blit(bus_left, position)
        elif direction == 'up':
            world.blit(bus_up, position)
    elif vehicle_type == 'car':
        if direction == 'right':
            world.blit(car_right, position)
        elif direction == 'down':
            world.blit(car_down, position)
        elif direction == 'left':
            world.blit(car_left, position)
        elif direction == 'up':
            world.blit(car_up, position)
    elif vehicle_type == 'truck':
        if direction == 'right':
            world.blit(truck_right, position)
        elif direction == 'down':
            world.blit(truck_down, position)
        elif direction == 'left':
            world.blit(truck_left, position)
        elif direction == 'up':
            world.blit(truck_up, position)


# Start coordinates
rightCordStart = [[1590, 830], [1590, 876], [1590, 496], [1590, 1590, 549], [1590, 235], [1590, 278]]


class Vehicle(pygame.sprite.Sprite):
    def __int__(self, lane, ):
        pygame.sprite.Sprite.__init__(self)


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
            dx, dy = prev_mouse_pos[0] - mouse_pos[0], prev_mouse_pos[1] - mouse_pos[1]
            camera.move_ip(dx, dy)
            camera.clamp_ip(world.get_rect())
            prev_mouse_pos = mouse_pos

        win.blit(world.subsurface(camera), (0, 0))
        pygame.display.flip()
