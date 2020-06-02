# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
import datetime
import random


class Requests_Elevators():

    def __init__(self, current_floor, next_floor):
        self.timestamp = datetime.datetime.utcnow() + datetime.timedelta(seconds= random.randint(0, 30))
        self.current_floor = current_floor
        self.next_floor = next_floor
        self.direction = self.calculate_direction(current_floor, next_floor)
        self.is_served = False
        self.passenger_inside = False

    def __str__(self):
        return ('Request from floor {} to floor {}').format(self.current_floor, self.next_floor)

    def set_order(self, order):
        self.order = order

    def calculate_direction(self, current_floor, next_floor):
        if next_floor > current_floor:
            return 1
        else:
            return -1
