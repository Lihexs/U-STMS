import os.path
import random
import time
import threading
import sys
import pygame
import pyautogui

pygame.init()

# Window view
win_width = 1920
win_height = 1080
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# World view
world_width = 3590
world_height = 2252
world = pygame.Surface((world_width, world_height))

bg = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Background', 'intersection.png')) \

scale = 1.5
scale_tl = 0.85

bg = pygame.transform.scale(bg, (win_width * scale, win_height * scale))

# Camera view
camera = pygame.Rect(0, 0, win_width, win_height)

# Background

# load all the images
bike_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'bike.png'))
bike_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'bike.png'))
bike_right = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'bike.png'))
bike_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'bike.png'))

bus_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'bus.png'))
bus_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'bus.png'))
bus_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'bus.png'))
bus_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'bus.png'))

car_down = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'car.png'))
car_left = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'car.png'))
car_right = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'car.png'))
car_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'car.png'))

truck_down = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'truck.png'))
truck_left = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'truck.png'))
truck_right = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'truck.png'))
truck_up = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'truck.png'))

traffic_light_green = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Signals', 'green.png'))
traffic_light_red = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Signals', 'red.png'))
traffic_light_yellow = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Signals', 'yellow.png'))

# scale all images according to the scale

bike_down = pygame.transform.scale(bike_down, (int(bike_down.get_width() * scale), int(bike_down.get_height() * scale)))
bike_left = pygame.transform.scale(bike_left, (int(bike_left.get_width() * scale), int(bike_left.get_height() * scale)))
bike_right = pygame.transform.scale(bike_right,
                                    (int(bike_right.get_width() * scale), int(bike_right.get_height() * scale)))
bike_up = pygame.transform.scale(bike_up, (int(bike_up.get_width() * scale), int(bike_up.get_height() * scale)))

bus_down = pygame.transform.scale(bus_down, (int(bus_down.get_width() * scale), int(bus_down.get_height() * scale)))
bus_left = pygame.transform.scale(bus_left, (int(bus_left.get_width() * scale), int(bus_left.get_height() * scale)))
bus_right = pygame.transform.scale(bus_right, (int(bus_right.get_width() * scale), int(bus_right.get_height() * scale)))
bus_up = pygame.transform.scale(bus_up, (int(bus_up.get_width() * scale), int(bus_up.get_height() * scale)))

car_down = pygame.transform.scale(car_down, (int(car_down.get_width() * scale), int(car_down.get_height() * scale)))
car_left = pygame.transform.scale(car_left, (int(car_left.get_width() * scale), int(car_left.get_height() * scale)))
car_right = pygame.transform.scale(car_right, (int(car_right.get_width() * scale), int(car_right.get_height() * scale)))
car_up = pygame.transform.scale(car_up, (int(car_up.get_width() * scale), int(car_up.get_height() * scale)))

truck_down = pygame.transform.scale(truck_down,
                                    (int(truck_down.get_width() * scale), int(truck_down.get_height() * scale)))
truck_left = pygame.transform.scale(truck_left,
                                    (int(truck_left.get_width() * scale), int(truck_left.get_height() * scale)))
truck_right = pygame.transform.scale(truck_right,
                                     (int(truck_right.get_width() * scale), int(truck_right.get_height() * scale)))
truck_up = pygame.transform.scale(truck_up, (int(truck_up.get_width() * scale), int(truck_up.get_height() * scale)))

traffic_light_green = pygame.transform.scale(traffic_light_green, (
int(traffic_light_green.get_width() * scale_tl), int(traffic_light_green.get_height() * scale_tl)))
traffic_light_red = pygame.transform.scale(traffic_light_red, (
int(traffic_light_red.get_width() * scale_tl), int(traffic_light_red.get_height() * scale_tl)))
traffic_light_yellow = pygame.transform.scale(traffic_light_yellow, (
int(traffic_light_yellow.get_width() * scale_tl), int(traffic_light_yellow.get_height() * scale_tl)))

speed = 10
#Traffic Light class
class Traffic_Light:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.time = 0

    def set_color(self, color):
        self.color = color

    def reset_time(self):
        self.time = 0

    def update_time(self):
        self.time += 1

    def get_time(self):
        return self.time

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

# create traffic lights objects
# 0 - red, 1 - yellow, 2 - green
traffic_light1 = Traffic_Light((945, 70), 0)
traffic_light2 = Traffic_Light((1130, 75), 0)
traffic_light3 = Traffic_Light((945, 290), 0)
traffic_light4 = Traffic_Light((945, 670), 0)
traffic_light5 = Traffic_Light((1130, 295), 0)
traffic_light6 = Traffic_Light((1130, 670), 0)
traffic_light7 = Traffic_Light((945, 450), 0)
traffic_light8 = Traffic_Light((1130, 450), 0)

traffic_lights = [traffic_light1, traffic_light2, traffic_light3, traffic_light4, traffic_light5, traffic_light6,
                  traffic_light7, traffic_light8]

# create the traffic lights as objects




traffic_light_color1 = traffic_light_green
traffic_light_color2 =traffic_light_green
traffic_light_color3 = traffic_light_green
traffic_light_color4 = traffic_light_green
traffic_light_color5 = traffic_light_green
traffic_light_color6 = traffic_light_green
traffic_light_color7 = traffic_light_green
traffic_light_color8 = traffic_light_green


# configure the traffic light to the red sprite

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






class Vehicle(pygame.sprite.Sprite):
    def __int__(self, lane, ):
        pygame.sprite.Sprite.__init__(self)

# Start coordinates
rightCordStart = [[1590, 830], [1590, 876], [1590, 496], [1590, 1590, 549], [1590, 235], [1590, 278]]

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
        # blit the traffic light
        # win.blit(traffic_light_color1, (traffic_light1.x, traffic_light1.y))
        # win.blit(traffic_light_color2, (traffic_light2.x, traffic_light2.y))
        # win.blit(traffic_light_color3, (traffic_light3.x, traffic_light3.y))
        # win.blit(traffic_light_color4, (traffic_light4.x, traffic_light4.y))
        # win.blit(traffic_light_color5, (traffic_light5.x, traffic_light5.y))
        # win.blit(traffic_light_color6, (traffic_light6.x, traffic_light6.y))
        # win.blit(traffic_light_color7, (traffic_light7.x, traffic_light7.y))
        # win.blit(traffic_light_color8, (traffic_light8.x, traffic_light8.y))
        for traffic_light in traffic_lights:
            if traffic_light.get_color() == 0:
                win.blit(traffic_light_red, traffic_light.get_position())
            elif traffic_light.color == 2:
                win.blit(traffic_light_green, traffic_light.get_position())
            elif traffic_light.color == 1:
                win.blit(traffic_light_yellow, traffic_light.get_position())
        # blit the vehicles
        # for vehicle in vehicles:
        #     pass

        pygame.display.flip()
