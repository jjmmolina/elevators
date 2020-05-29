# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
# Direction 1 => up; -1 => down; None => stopping
class Elevator():
    def __init__(self, id):
        self.id = id
        self.floor = 0
        self.direction = None
        self.default_elevator = False
        self.available = True
        self.requests = 0

    def got_to_up(self, next_floor):
        self.available = False
        # TODO set timer to simulate the trip
        self.floor = next_floor
        self.available = True
        return 1

    def got_to_down(self, next_floor):
        self.available = False
        # TODO set timer to simulate the trip
        self.floor = next_floor
        self.available = True
        return 1

    def move(self, building):
        """Moves one floor in self.direction."""
        building.floors[self.floor].remove(self)
        self.floor += self.direction
        building.floors[self.floor].append(self)
        print("On floor {}...".format(self.floor))

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



