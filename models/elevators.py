# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
import json

from threading import Lock
from time import sleep

global_lock = Lock()

# Direction 1 => up; -1 => down; None => stopped
class Elevator():
    requests_to_serve = []
    def __init__(self, id):
        self.id = id
        self.floor = 0
        self.direction = None
        self.num_requests = 0
        self.passengers = 0


    def run(self, building):
        while len(building.requests) is not 0:
            if (self.num_requests <= (len(building.floors) / len(building.elevators))):
                while global_lock.locked():
                    continue

                global_lock.acquire()
                # Si estoy parado, obtengo la petición más antigua
                if self.direction is None:
                    building.requests = sorted(building.requests, key=lambda request: request.timestamp)
                    request = building.requests[0]

                # Si no, la que esté más cerca de mi en mi dirección
                else:
                    building.requests = sorted(building.requests, key=lambda request: request.current_floor)
                    request = building.get_request(self.direction)
                if request is not None:
                    request.is_served = True
                    new_request = []
                    for req in building.requests:
                        if not req.is_served:
                            new_request.append(req)
                    building.requests = new_request

                    building.move_elevator(self, request.current_floor)
                    self.num_requests += 1
                    self.passengers += 1
                    self.requests_to_serve.append(request)

                    print("ELEVATOR NUMBER {} ARRIVES TO FLOOR {} TO GET ITS FIRST PASSENGER".format(self.id,
                                                                                                     request.current_floor))
                    request.passenger_inside = True
                    # Elevator stops at this floor
                    sleep(0.5)
                    building.move_elevator(self, request.next_floor)

                global_lock.release()





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
        if (float(self.num_requests) < (floors / elevators)):
            return True
        return False

    def set_direction(self, to_floor):
        if self.floor <= to_floor:
            self.direction = 1
        else:
            self.direction = -1



