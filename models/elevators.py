# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
# Direction 1 => up; -1 => down; None => stopping
class Elevator():
    requests_to_serve = []
    def __init__(self, id):
        self.id = id
        self.floor = 0
        self.direction = None
        self.default_elevator = False
        self.available = True
        self.requests = 0
        self.passengers = 0


    def move(self, building):
        """Moves one floor in self.direction."""
        building.floors[self.floor].remove(self)
        self.floor += self.direction
        building.floors[self.floor].append(self)
        print("On floor {}...".format(self.floor))
        self.check_requests_elevators(building, self.floor)

    def check_requests_elevators(self, building, floor):
        for request in building.requests:
            if (request.current_floor == floor) & (request.direction == self.direction):
                building.floors.remove(request)
                self.passengers += 1
                self.requests_to_serve.append(request)



    def is_elevator_in_requests_floor(self, request_floor):
        return (request_floor == self.floor)

    def is_default_elevator(self):
        return self.default_elevator

    def is_my_direction(self, direction):
        return self.direction == direction

    def is_available(self):
        return self.available

    def set_direction(self, to_floor):
        if self.floor < to_floor:
            self.direction = 1
        else:
            self.direction = -1



