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
        self.num_requests = 0
        self.passengers = 0


    def move(self, building):
        """Moves one floor in self.direction."""
        building.floors[self.floor].remove(self)
        self.floor += self.direction
        building.floors[self.floor].append(self)
        print("On floor {} with {} passengers".format(self.floor, self.passengers))


    def is_elevator_in_requests_floor(self, request_floor):
        return (request_floor == self.floor)

    def is_my_direction(self, direction):
        return self.direction == direction

    def is_available(self, floors, elevators):
        if self.num_requests < int(floors / elevators):
            return True
        return False

    def set_direction(self, to_floor):
        if self.floor <= to_floor:
            self.direction = 1
        else:
            self.direction = -1



