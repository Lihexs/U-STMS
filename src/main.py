import os.path
import random
import time
import threading
import sys
import pygame
import pyautogui

pygame.init()

scale = 1.5
scale_tl = 0.85

speed = 10

buffer_size = 5

# Window view
win_width = 1920
win_height = 1080
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# World view
world_width = 3590
world_height = 2252
world = pygame.Surface((world_width, world_height))

bg = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Background', 'intersection.png'))

bg = pygame.transform.scale(bg, (win_width * scale, win_height * scale))

# Camera view
camera = pygame.Rect(0, 0, win_width, win_height)

world.blit(bg, (0, 0))

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


# Traffic Light class
class Traffic_Light:
    def __init__(self, position, color, arrival_direction, starting_coords):
        self.position = position
        self.color = color
        self.arrival_direction = arrival_direction
        self.starting_coords = starting_coords
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

    def get_arrival_direction(self):
        return self.arrival_direction

    def get_starting_coords(self):
        return self.starting_coords

    def set_starting_coords(self, starting_coords):
        self.starting_coords = starting_coords


# create traffic lights objects
# 0 - red, 1 - yellow, 2 - green
# 0 - left, 1 - right, 2 - up, 3 - down
traffic_light1 = Traffic_Light((945, 70), 0, 3, (994, -50))
traffic_light2 = Traffic_Light((945, 290), 0, 1, (-50, 230))
traffic_light3 = Traffic_Light((945, 450), 0, 3, None)
traffic_light4 = Traffic_Light((945, 670), 0, 1, (-50, 602))
traffic_light5 = Traffic_Light((1130, 75), 0, 0, (1570, 173))
traffic_light6 = Traffic_Light((1130, 295), 0, 2, None)
traffic_light7 = Traffic_Light((1130, 450), 0, 0, (1570, 544))
traffic_light8 = Traffic_Light((1130, 670), 0, 2, (1076, 1000))

# coords 0 direction - up
# coords 1 direction - down
# coords 2 direction - left
# coords 3 direction - right
# coords 4 direction - left
# coords 5 direction - right

traffic_lights = [traffic_light1, traffic_light2, traffic_light3, traffic_light4, traffic_light5, traffic_light6,
                  traffic_light7, traffic_light8]

# Mouse movement
dragging = False
prev_mouse_pos = (0, 0)

vehicle_types = ['bike', 'bus', 'car', 'truck']
direction_dict = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}


class Vehicle:
    def __init__(self, speed, traffic_light, type):
        pygame.sprite.Sprite.__init__(self)
        self.passengers = 0
        if type == 1:
            self.passengers = random.randint(0, 50)
        self.position = position
        self.type = type
        self.speed = speed
        self.direction = traffic_light.arrival_direction
        self.traffic_light = traffic_light
        self.stopped = False

    def get_position(self):
        return self.position

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def set_speed(self, speed):
        self.speed = speed

    def set_direction(self, direction):
        self.direction = direction

    def move(self, direction):
        if direction == 'right':
            position_x = self.get_position()[0] + speed
            position_y = self.get_position()[1]
            position = (position_x, position_y)
            self.set_position(position)
        elif direction == 'down':
            position_x = self.get_position()[0]
            position_y = self.get_position()[1] + speed
            position = (position_x, position_y)
            self.set_position(position)
        elif direction == 'left':
            position_x = self.get_position()[0] - speed
            position_y = self.get_position()[1]
            position = (position_x, position_y)
            self.set_position(position)
        elif direction == 'up':
            position_x = self.get_position()[0]
            position_y = self.get_position()[1] - speed
            position = (position_x, position_y)
            self.set_position(position)

    def within_buffer_move(self, buffer_size):
        dist = ((self.position[0] - traffic_light.get_position()[0]) ** 2 + (
                self.position[0] - traffic_light.get_position()[1]) ** 2) ** 0.5
        return dist <= buffer_size


# 0 - left, 1 - right, 2 - up, 3 - down
# 0 - car, 1 - bus, 2 - truck, 3 - bike, 4 - ambulance


car1 = Vehicle(speed, traffic_light1, 0)
car2 = Vehicle(speed, traffic_light2, 0)
car3 = Vehicle(speed, traffic_light3, 0)
car4 = Vehicle(speed, traffic_light4, 0)
car5 = Vehicle(speed, traffic_light5, 1)
car6 = Vehicle(speed, traffic_light6, 1)
car7 = Vehicle(speed, traffic_light7, 1)
car8 = Vehicle(speed, traffic_light8, 1)
car9 = Vehicle(speed, traffic_light1, 2)
car10 = Vehicle(speed, traffic_light2, 2)
car11 = Vehicle(speed, traffic_light3, 2)
car12 = Vehicle(speed, traffic_light4, 2)
car13 = Vehicle(speed, traffic_light5, 3)
car14 = Vehicle(speed, traffic_light6, 3)
car15 = Vehicle(speed, traffic_light7, 3)
car16 = Vehicle(speed, traffic_light8, 3)
car17 = Vehicle(speed, traffic_light1, 4)
car18 = Vehicle(speed, traffic_light2, 4)
car19 = Vehicle(speed, traffic_light3, 4)
car20 = Vehicle(speed, traffic_light4, 4)

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

        # blit the traffic lights
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
