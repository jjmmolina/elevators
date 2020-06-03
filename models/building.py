# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
import threading

from models.elevators import Elevator
from models.requests_elevators import Requests_Elevators
from time import sleep
from threading import Thread



class Building():
    elevators = []
    floors = []
    current_order = 0

    def __init__(self, num_floors, num_elevators):
        if num_floors < 1 or num_elevators < 1:
            raise (ValueError, "Invalid parameters"
                               "Floor and elevator counts should be equal or greater than 1.")

        self.elevators = [Elevator(i) for i in range(num_elevators)]
        self.floors = [[] for _ in range(num_floors + 1)]
        self.floors[0] = self.elevators[:]
        self.requests = []

    def __str__(self):
        return ("{} floors building with {} elevators on floors "
                .format(len(self.floors), len(self.elevators)) +
                ', '.join(str(elevator.floor) for elevator in self.elevators))

    def __repr__(self):
        return ("<Building with {} floors and {} elevators>"
                .format(len(self.floors), len(self.elevators)))

    def add_request(self, current_floor, next_floor):
        last_request = Requests_Elevators(current_floor, next_floor)
        self.current_order += 1
        last_request.set_order(self.current_order)
        self.requests.append(last_request)

    def validate_floor(self, floor):
        if floor >= len(self.floors):
            raise ValueError("Invalid floor {}, this building only has {} floors.".format(floor, len(self.floors) - 1))

    def validate_direction(self, floor, direction):
        if direction not in (1, -1):
            raise ValueError("Direction only accepts 1 or -1, not {}".format(direction))
        # At each floor — except the first one and the last one, the request can be made in two directions.
        if ((floor == 0) & (direction == -1)) | ((floor == len(self.floors) - 1) & (direction == 1)):
            raise ValueError("Invalid direction {} for floor {}.".format(direction, floor))

    def validate_floor_elevator_direction(self, elevator, floor):
        if elevator.direction is None:
            return True
        # It is not possible to choose a floor that goes in the opposite direction of the outside call
        if ((elevator.direction == 1) & (floor < elevator.floor)) | (
                (elevator.direction == -1) & (floor > elevator.floor)):
            raise ValueError(
                "Invalid floor {}, this elevator goes to the other direction {}.".format(floor, elevator.direction))

    def move_elevator(self, elevator, to_floor):
        """Send elevator to floor, moving one floor at a time."""
        self.validate_floor(to_floor)
        if elevator.direction is not None:
            self.validate_floor_elevator_direction(elevator, to_floor)
        print("Elevator {} moving with {} passengers.".format(elevator.id, elevator.passengers))
        elevator.set_direction(to_floor)

        for _ in (range(elevator.floor, to_floor)
        if elevator.direction == 1 else range(elevator.floor, to_floor, -1)):
            elevator.move(self)
            self._check_passengers_in_current_floor(elevator, elevator.floor)

        print("Elevator {} arrives to floor {}".format(elevator.id, to_floor))
        if elevator.passengers == 0:
            elevator.requests_to_serve = []
            elevator.direction = None
            return True


    def _check_passengers_in_current_floor(self, elevator, floor):
        for request in elevator.requests_to_serve:
            if ((request.next_floor == floor) & (request.passenger_inside)):
                request.passenger_inside = False
                # Remove request in the list
                new_request = []
                for req in elevator.requests_to_serve:
                    if not req.passenger_inside:
                        new_request.append(req)
                elevator.requests_to_serve = new_request
                elevator.passengers -= 1


    def get_request(self, direction):
        # Get request in the same direction
        my_requests = [request for request in self.requests if request.direction == direction]
        my_requests = sorted(my_requests, key=lambda ele: ele.current_floor)
        if len(my_requests) == 0:
            return None
        else:
            return my_requests[0]


    def call_elevator(self, floor, direction):
        """Chooses and returns an elevator after moving it to floor.
        Floor should be the floor the elevator is called to.
        Direction should indicate which way the user wants to travel, values should be 1 or -1."""
        self.validate_floor(floor)
        self.validate_direction(floor, direction)

        # Check if there's any elevators on the current floor
        if self.floors[floor]:
            elevator = self.get_elevator(self.floors[floor], direction)
            if elevator is None:
                return None
            else:
                print("Elevator {} on floor {}".format(elevator.id, floor))
                return elevator
        # If not, look for an elevator in the rest of floors
        check_floors = []
        for elev in self.floors:
            for ele in elev:
                check_floors.append(ele)
        if check_floors is not None:
            elevator = self.get_elevator(check_floors, direction)
            if elevator is None:
                return None
        else:
            raise Exception("Cannot find elevators.")

        self.move_elevator(elevator, floor)
        elevator.num_requests += 1
        elevator.passengers += 1
        return elevator

    def move_passengers(self):
        for elevator in self.elevators:
            Thread(target=elevator.run, args=(self,)).start()



