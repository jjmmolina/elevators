# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
from models.requests_elevators import Requests_Elevators


class Building():
    requests = []
    elevators = []
    floors = []
    current_order = 0

    def __init__(self, floors, elevators):
        self.floors = floors
        self.elevators = elevators

    def add_request(self, current_floor, next_floor):
        last_request = Requests_Elevators(current_floor, next_floor)
        last_request.set_order(++self.current_order)
        self.requests.append(last_request)

    def is_available_elevator(self):
        #If there’s no available elevator to answer a request, the request is cancelled.
        pass
