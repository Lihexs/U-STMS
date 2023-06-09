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

speed = 1

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

ambulance_down = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'down', 'ambulance.png'))
ambulance_left = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'left', 'ambulance.png'))
ambulance_right = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'right', 'ambulance.png'))
ambulance_up = pygame.image.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Vehicles', 'up', 'ambulance.png'))

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


ambulance_down = pygame.transform.scale(ambulance_down,
                                    (int(ambulance_down.get_width() * 2*scale), int(ambulance_down.get_height() * 2*scale)))
ambulance_left = pygame.transform.scale(ambulance_left,
                                    (int(ambulance_left.get_width() * 2*scale), int(ambulance_left.get_height() * 2*scale)))
ambulance_right = pygame.transform.scale(ambulance_right,
                                     (int(ambulance_right.get_width() * 2 * scale), int(ambulance_right.get_height() * 2 * scale)))
ambulance_up = pygame.transform.scale(ambulance_up, (int(ambulance_up.get_width() * 2 * scale), int(ambulance_up.get_height() * 2 *scale)))



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
        self.vehicles = []  # Vehicle list of the traffic light lane

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def pop_vehicle(self):
        return self.vehicles.pop(0)

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
traffic_light3 = Traffic_Light((945, 450), 0, 3, (0, 0))
traffic_light4 = Traffic_Light((945, 670), 0, 1, (-50, 602))
traffic_light5 = Traffic_Light((1130, 75), 0, 0, (1570, 173))
traffic_light6 = Traffic_Light((1130, 295), 0, 2, (0, 0))
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

def dist(pos1, pos2):
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

class Vehicle:
    def __init__(self, speed, traffic_light, type):
        pygame.sprite.Sprite.__init__(self)
        self.passengers = 0
        if type == 1:
            self.passengers = random.randint(0, 50)
        self.type = type
        self.speed = speed
        self.position = traffic_light.get_starting_coords()
        self.direction = traffic_light.arrival_direction
        self.traffic_light = traffic_light
        traffic_light.add_vehicle(self)
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

    def set_speed(self, speed1):
        self.speed = speed1

    def set_direction(self, direction):
        self.direction = direction

    def set_traffic_light(self, traffic_light11):
        self.traffic_light = traffic_light11


    # 0 - left, 1 - right, 2 - up, 3 - down
    # 0 - red, 1 - yellow, 2 - green

    def move(self, direction):
        if self.direction == 2 and self.traffic_light.position[1] > self.position[1]:
            self.set_traffic_light(traffic_light6)
        if self.direction == 3 and self.traffic_light.position[1] < self.position[1]:
            self.set_traffic_light(traffic_light3)
        if self.traffic_light.color == 0 and direction == 0 and self.traffic_light.position[0] == self.position[0]:
            pass
        if len(self.traffic_light.vehicles) > 1 and self.traffic_light.vehicles.index(self) != 0 and dist(self.get_position(),
                                                                 self.traffic_light.vehicles[self.traffic_light.vehicles.index(self) - 1].get_position()) < 150:
            pass
        elif self.traffic_light.color == 0 and direction == 1 and self.traffic_light.position[0] == self.position[
            0] + 50:
            pass
        elif self.traffic_light.color == 0 and direction == 2 and self.traffic_light.position[1] == self.position[1]:
            pass
        elif self.traffic_light.color == 0 and direction == 3 and self.traffic_light.position[1] == self.position[
            1] + 25:
            pass
        elif direction == 0:
            self.set_position((self.get_position()[0] - self.get_speed(), self.get_position()[1]))
        elif direction == 1:
            self.set_position((self.get_position()[0] + self.get_speed(), self.get_position()[1]))
        elif direction == 2:
            self.set_position((self.get_position()[0], self.get_position()[1] - self.get_speed()))
        elif direction == 3:
            self.set_position((self.get_position()[0], self.get_position()[1] + self.get_speed()))


# 0 - left, 1 - right, 2 - up, 3 - down

# 0 - car, 1 - bus, 2 - truck, 3 - bike, 4 - ambulance


car1 = Vehicle(speed, traffic_light1, 0)
car2 = Vehicle(speed, traffic_light2, 0)
car3 = Vehicle(speed, traffic_light4, 0)
car4 = Vehicle(speed, traffic_light4, 0)
car5 = Vehicle(speed, traffic_light5, 1)
car6 = Vehicle(speed, traffic_light2, 1)
car7 = Vehicle(speed, traffic_light7, 1)
car8 = Vehicle(speed, traffic_light8, 1)
car9 = Vehicle(speed, traffic_light1, 2)
car10 = Vehicle(speed, traffic_light2, 2)
car11 = Vehicle(speed, traffic_light1, 2)
car12 = Vehicle(speed, traffic_light4, 2)
car13 = Vehicle(speed, traffic_light5, 3)
car14 = Vehicle(speed, traffic_light8, 3)
car15 = Vehicle(speed, traffic_light7, 3)
car16 = Vehicle(speed, traffic_light8, 3)
car17 = Vehicle(speed, traffic_light1, 1)
car18 = Vehicle(speed, traffic_light2, 2)
car19 = Vehicle(speed, traffic_light5, 2)
car20 = Vehicle(speed, traffic_light4, 3)

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10,
        car11, car12, car13, car14, car15, car16, car17, car18, car19, car20]

action_1_1 = {
    'green': ['tls6'],
    'red': ['tls2', 'tls1', 'tls5']
}

action_1_2 = {
    'green': ['tls5'],
    'red': ['tls6', 'tls2', 'tls1']
}

action_1_3 = {
    'green': ['tls2'],
    'red': ['tls1', 'tls5', 'tls6']
}

action_1_4 = {
    'green': ['tls1'],
    'red': ['tls2', 'tls5', 'tls6']
}

action_1_5 = {
    'green': ['tls6', 'tls1'],
    'red': ['tls2', 'tls5']
}

action_1_6 = {
    'green': ['tls5', 'tls2'],
    'red': ['tls6', 'tls1']
}
action_2_1 = {
    'green': ['tls7'],
    'red': ['tls3', 'tls4', 'tls8']
}

action_2_2 = {
    'green': ['tls8'],
    'red': ['tls7', 'tls3', 'tls4']
}

action_2_3 = {
    'green': ['tls3'],
    'red': ['tls4', 'tls8', 'tls7']
}

action_2_4 = {
    'green': ['tls4'],
    'red': ['tls3', 'tls8', 'tls7']
}

action_2_5 = {
    'green': ['tls7', 'tls4'],
    'red': ['tls3', 'tls8']
}

action_2_6 = {
    'green': ['tls8', 'tls3'],
    'red': ['tls7', 'tls4']
}

traffic_lights_1 = {
    "tls1": {
        "num_cars": 10,
        "num_buses": 2,
        "num_of_passengers": 30,
        "num_ambulances": 0,
        "waiting": 1,
        "is_green": 0
    },
    "tls2": {
        "num_cars": 5,
        "num_buses": 1,
        "num_of_passengers": 20,
        "num_ambulances": 0,
        "waiting": 0,
        "is_green": 0
    },
    "tls3": {
        "num_cars": 8,
        "num_buses": 0,
        "num_of_passengers": 15,
        "num_ambulances": 1,
        "waiting": 2,
        "is_green": 1
    },
    "tls4": {
        "num_cars": 5,
        "num_buses": 1,
        "num_of_passengers": 20,
        "num_ambulances": 0,
        "waiting": 0,
        "is_green": 1
    },
    "tls5": {
        "num_cars": 3,
        "num_buses": 0,
        "num_of_passengers": 10,
        "num_ambulances": 0,
        "waiting": 1,
        "is_green": 0
    },
    "tls6": {
        "num_cars": 6,
        "num_buses": 2,
        "num_of_passengers": 25,
        "num_ambulances": 1,
        "waiting": 0,
        "is_green": 0
    },
    "tls7": {
        "num_cars": 2,
        "num_buses": 0,
        "num_of_passengers": 5,
        "num_ambulances": 0,
        "waiting": 0,
        "is_green": 0
    },
    "tls8": {
        "num_cars": 7,
        "num_buses": 1,
        "num_of_passengers": 18,
        "num_ambulances": 0,
        "waiting": 2,
        "is_green": 1
    }
}


def evaluate(traffic_lights_info):
    # Constants to weigh the importance of different factors
    CAR_WEIGHT = 1
    BUS_WEIGHT = 15
    AMBULANCE_WEIGHT = 1000
    WAITING_BONUS = 0.5
    GREEN__PENALTY = 10

    # Calculate the current "congestion" and "waiting" scores for each direction
    scores = {direction: (CAR_WEIGHT * counts['num_cars'] +
                          BUS_WEIGHT * counts['num_buses'] + counts['num_of_passengers'] / 2 +
                          AMBULANCE_WEIGHT * counts['num_ambulances'] +
                          WAITING_BONUS * (counts['waiting'] +
                                           GREEN__PENALTY * counts['is_green'])) for direction, counts in
              traffic_lights_info.items()}

    # Split scores into 2 intersections
    intersaction1 = {key: value for key, value in scores.items() if key in ['tls1', 'tls2', 'tls5', 'tls6']}
    intersaction2 = {key: value for key, value in scores.items() if key in ['tls3', 'tls4', 'tls7', 'tls8']}

    # Find the key with the max value in each intersection
    max_key_inter1 = max(intersaction1, key=intersaction1.get)
    max_key_inter2 = max(intersaction2, key=intersaction2.get)

    # Find the max sum of pair values in each intersection
    if intersaction1['tls1'] + intersaction1['tls6'] > intersaction1['tls2'] + intersaction1['tls5']:
        max_key_duoes1 = ('tls1', 'tls6')
    else:
        max_key_duoes1 = ('tls2', 'tls5')

    if intersaction2['tls3'] + intersaction2['tls8'] > intersaction2['tls4'] + intersaction2['tls7']:
        max_key_duoes2 = ('tls3', 'tls8')
    else:
        max_key_duoes2 = ('tls4', 'tls7')

    duoes1 = (max_key_duoes1, max_key_inter1)
    duoes2 = (max_key_duoes2, max_key_inter2)

    chosen_interation1 = random.choice(duoes1)
    chosen_interation2 = random.choice(duoes2)

    return chosen_interation1, chosen_interation2


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
        num_of_ambluances1 = 0
        num_of_bus1 = 0
        num_of_passengers1 = 0
        for vehicle in traffic_light1.vehicles:
            if vehicle.type == 4:
                num_of_ambluances1 += 1
            if vehicle.type == 1:
                num_of_bus1 += 1
                num_of_passengers1 += vehicle.passengers

        num_of_ambluances2 = 0
        num_of_bus2 = 0
        num_of_passengers2 = 0
        for vehicle in traffic_light2.vehicles:
            if vehicle.type == 4:
                num_of_ambluances2 += 1
            if vehicle.type == 1:
                num_of_bus2 += 1
                num_of_passengers2 += vehicle.passengers

        num_of_ambluances3 = 0
        num_of_bus3 = 0
        num_of_passengers3 = 0
        for vehicle in traffic_light3.vehicles:
            if vehicle.type == 4:
                num_of_ambluances3 += 1
            if vehicle.type == 1:
                num_of_bus3 += 1
                num_of_passengers3 += vehicle.passengers

        num_of_ambluances4 = 0
        num_of_bus4 = 0
        num_of_passengers4 = 0
        for vehicle in traffic_light4.vehicles:
            if vehicle.type == 4:
                num_of_ambluances4 += 1
            if vehicle.type == 1:
                num_of_bus4 += 1
                num_of_passengers4 += vehicle.passengers

        num_of_ambluances5 = 0
        num_of_bus5 = 0
        num_of_passengers5 = 0
        for vehicle in traffic_light5.vehicles:
            if vehicle.type == 4:
                num_of_ambluances5 += 1
            if vehicle.type == 1:
                num_of_bus5 += 1
                num_of_passengers5 += vehicle.passengers

        num_of_ambluances6 = 0
        num_of_bus6 = 0
        num_of_passengers6 = 0
        for vehicle in traffic_light6.vehicles:
            if vehicle.type == 4:
                num_of_ambluances6 += 1
            if vehicle.type == 1:
                num_of_bus6 += 1
                num_of_passengers6 += vehicle.passengers

        num_of_ambluances7 = 0
        num_of_bus7 = 0
        num_of_passengers7 = 0
        for vehicle in traffic_light7.vehicles:
            if vehicle.type == 4:
                num_of_ambluances7 += 1
            if vehicle.type == 1:
                num_of_bus7 += 1
                num_of_passengers7 += vehicle.passengers

        num_of_ambluances8 = 0
        num_of_bus8 = 0
        num_of_passengers8 = 0
        for vehicle in traffic_light8.vehicles:
            if vehicle.type == 4:
                num_of_ambluances8 += 1
            if vehicle.type == 1:
                num_of_bus8 += 1
                num_of_passengers8 += vehicle.passengers

        traffic_lights_info_orig = {
            "tls1": {
                "num_cars": len(traffic_light1.vehicles),
                "num_buses": num_of_bus1,
                "num_of_passengers": num_of_passengers1,
                "num_ambulances": num_of_ambluances1,
                "waiting": traffic_light1.get_time(),
                "is_green": 0 if traffic_light1.get_color() == 2 else 1
            },
            "tls2": {
                "num_cars": len(traffic_light2.vehicles),
                "num_buses": num_of_bus2,
                "num_of_passengers": num_of_passengers2,
                "num_ambulances": num_of_ambluances2,
                "waiting": traffic_light2.get_time(),
                "is_green": 0 if traffic_light2.get_color() == 2 else 1
            },
            "tls3": {
                "num_cars": len(traffic_light3.vehicles),
                "num_buses": num_of_bus3,
                "num_of_passengers": num_of_passengers3,
                "num_ambulances": num_of_ambluances3,
                "waiting": traffic_light3.get_time(),
                "is_green": 0 if traffic_light3.get_color() == 2 else 1
            },
            "tls4": {
                "num_cars": len(traffic_light4.vehicles),
                "num_buses": num_of_bus4,
                "num_of_passengers": num_of_passengers4,
                "num_ambulances": num_of_ambluances4,
                "waiting": traffic_light4.get_time(),
                "is_green": 0 if traffic_light4.get_color() == 2 else 1
            },
            "tls5": {
                "num_cars": len(traffic_light5.vehicles),
                "num_buses": num_of_bus5,
                "num_of_passengers": num_of_passengers5,
                "num_ambulances": num_of_ambluances5,
                "waiting": traffic_light5.get_time(),
                "is_green": 0 if traffic_light5.get_color() == 2 else 1
            },
            "tls6": {
                "num_cars": len(traffic_light6.vehicles),
                "num_buses": num_of_bus6,
                "num_of_passengers": num_of_passengers6,
                "num_ambulances": num_of_ambluances6,
                "waiting": traffic_light6.get_time(),
                "is_green": 0 if traffic_light6.get_color() == 2 else 1
            },
            "tls7": {
                "num_cars": len(traffic_light7.vehicles),
                "num_buses": num_of_bus7,
                "num_of_passengers": num_of_passengers7,
                "num_ambulances": num_of_ambluances7,
                "waiting": traffic_light7.get_time(),
                "is_green": 0 if traffic_light7.get_color() == 2 else 1
            },
            "tls8": {
                "num_cars": len(traffic_light8.vehicles),
                "num_buses": num_of_bus8,
                "num_of_passengers": num_of_passengers8,
                "num_ambulances": num_of_ambluances8,
                "waiting": traffic_light8.get_time(),
                "is_green": 0 if traffic_light8.get_color() == 2 else 1
            }
        }

        for traffic_light in traffic_lights:
            traffic_light.set_color(0)

        dou1, dou2 = evaluate(traffic_lights_info_orig)

        for tl in dou1:
            if tl == 'tls1':
                traffic_light1.set_color(2)
                traffic_light1.reset_time()
            elif tl == 'tls2':
                traffic_light2.set_color(2)
                traffic_light2.reset_time()
            elif tl == 'tls3':
                traffic_light3.set_color(2)
                traffic_light3.reset_time()
            elif tl == 'tls4':
                traffic_light4.set_color(2)
                traffic_light4.reset_time()
            elif tl == 'tls5':
                traffic_light5.set_color(2)
                traffic_light5.reset_time()
            elif tl == 'tls6':
                traffic_light6.set_color(2)
                traffic_light6.reset_time()
            elif tl == 'tls7':
                traffic_light7.set_color(2)
                traffic_light7.reset_time()
            elif tl == 'tls8':
                traffic_light8.set_color(2)
                traffic_light8.reset_time()

        for tl in dou2:
            if tl == 'tls1':
                traffic_light1.set_color(2)
                traffic_light1.reset_time()
            elif tl == 'tls2':
                traffic_light2.set_color(2)
                traffic_light2.reset_time()
            elif tl == 'tls3':
                traffic_light3.set_color(2)
                traffic_light3.reset_time()
            elif tl == 'tls4':
                traffic_light4.set_color(2)
                traffic_light4.reset_time()
            elif tl == 'tls5':
                traffic_light5.set_color(2)
                traffic_light5.reset_time()
            elif tl == 'tls6':
                traffic_light6.set_color(2)
                traffic_light6.reset_time()
            elif tl == 'tls7':
                traffic_light7.set_color(2)
                traffic_light7.reset_time()
            elif tl == 'tls8':
                traffic_light8.set_color(2)
                traffic_light8.reset_time()
        for vehicle in cars:
            vehicle.move(vehicle.get_direction())
        if dragging:
            mouse_pos = pygame.mouse.get_pos()
            dx, dy = prev_mouse_pos[0] - mouse_pos[0], prev_mouse_pos[1] - mouse_pos[1]
            camera.move_ip(dx, dy)
            camera.clamp_ip(world.get_rect())
            prev_mouse_pos = mouse_pos

        win.blit(world.subsurface(camera), (0, 0))

        # blit the traffic lights
        for traffic_light in traffic_lights:
            traffic_light.update_time()
            if traffic_light.get_color() == 0:
                win.blit(traffic_light_red, traffic_light.get_position())
            elif traffic_light.color == 2:
                win.blit(traffic_light_green, traffic_light.get_position())
            elif traffic_light.color == 1:
                win.blit(traffic_light_yellow, traffic_light.get_position())
        # blit the vehicles
        # for vehicle in vehicles:
        #     pass

        # blit the cars
        # 0 - left, 1 - right, 2 - up, 3 - down
        # 0 - car, 1 - bus, 2 - truck, 3 - bike, 4 - ambulance

        for car in cars:
            if car.type == 0 and car.get_direction() == 0:
                win.blit(car_left, car.get_position())
            elif car.type == 0 and car.get_direction() == 1:
                win.blit(car_right, car.get_position())
            elif car.type == 0 and car.get_direction() == 2:
                win.blit(car_up, car.get_position())
            elif car.type == 0 and car.get_direction() == 3:
                win.blit(car_down, car.get_position())
            elif car.type == 1 and car.get_direction() == 0:
                win.blit(bus_left, car.get_position())
            elif car.type == 1 and car.get_direction() == 1:
                win.blit(bus_right, car.get_position())
            elif car.type == 1 and car.get_direction() == 2:
                win.blit(bus_up, car.get_position())
            elif car.type == 1 and car.get_direction() == 3:
                win.blit(bus_down, car.get_position())
            elif car.type == 2 and car.get_direction() == 0:
                win.blit(truck_left, car.get_position())
            elif car.type == 2 and car.get_direction() == 1:
                win.blit(truck_right, car.get_position())
            elif car.type == 2 and car.get_direction() == 2:
                win.blit(truck_up, car.get_position())
            elif car.type == 2 and car.get_direction() == 3:
                win.blit(truck_down, car.get_position())
            elif car.type == 3 and car.get_direction() == 0:
                win.blit(bike_left, car.get_position())
            elif car.type == 3 and car.get_direction() == 1:
                win.blit(bike_right, car.get_position())
            elif car.type == 3 and car.get_direction() == 2:
                win.blit(bike_up, car.get_position())
            elif car.type == 3 and car.get_direction() == 3:
                win.blit(bike_down, car.get_position())
            elif car.type == 4 and car.get_direction() == 0:
                win.blit(ambulance_left, car.get_position())
            elif car.type == 4 and car.get_direction() == 1:
                win.blit(ambulance_right, car.get_position())
            elif car.type == 4 and car.get_direction() == 2:
                win.blit(ambulance_up, car.get_position())
            elif car.type == 4 and car.get_direction() == 3:
                win.blit(ambulance_down, car.get_position())

        # 0 - red, 1 - yellow, 2 - green

        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light1.set_color(2)
        #     traffic_light1.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light1.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light2.set_color(2)
        #     traffic_light2.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light3.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light4.set_color(2)
        #     traffic_light4.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light4.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light5.set_color(2)
        #     traffic_light5.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light5.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light6.set_color(2)
        #     traffic_light6.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light6.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light7.set_color(2)
        #     traffic_light7.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light7.set_color(0)
        #
        # rand_change_traffic_light = random.randint(0, 1000)
        # if rand_change_traffic_light == 0:
        #     traffic_light8.set_color(2)
        #     traffic_light8.reset_time()
        # elif rand_change_traffic_light == 1:
        #     traffic_light8.set_color(0)



        pygame.display.flip()
