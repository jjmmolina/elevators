# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
#Direction 1 => up; 0 => down
class Elevator():
    def __init__(self, default_elevator, available):
        self.floor = 1
        self.direction = 1
        self.default_elevator = default_elevator
        self.available = True

    def got_to_up(self, next_floor):
        self.available = False
        # TODO set timer to simulate the trip
        self.floor = next_floor
        pass

    def got_to_down(self, next_floor):
        self.available = False
        # TODO set timer to simulate the trip
        self.floor = next_floor
        pass

    def is_elevator_in_requests_floor(self, request_floor):
        return (request_floor == self.floor)
    def is_default_elevator(self):
        return self.default_elevator

    def is_my_direction(self, direction):
        return self.direction == direction

    def is_available(self):
        return self.available
