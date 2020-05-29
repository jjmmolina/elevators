# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
from models.elevators import Elevator
from models.requests_elevators import Requests_Elevators
from time import sleep


class Building():
    requests = []
    elevators = []
    floors = []
    current_direction = 0

    def __init__(self, num_floors, num_elevators):
        if num_floors < 1 or num_elevators < 1:
              raise (ValueError, "Invalid parameters"
                                   "Floor and elevator counts should be equal or greater than 1.")

        self.elevators = [Elevator(i) for i in range(num_elevators)]
        self.floors = [[] for _ in range(num_floors+1)]
        self.floors[0] = self.elevators[:]
        self.elevators[0].default_elevator = True

    def __str__(self):
        return ("{} floors building with {} elevators on floors "
                .format(len(self.floors),len(self.elevators)) +
                ', '.join(str(elevator.floor) for elevator in self.elevators))

    def __repr__(self):
        return ("<Building with {} floors and {} elevators>"
                .format(len(self.floors), len(self.elevators)))

    def _add_request(self, current_floor):
        last_request = Requests_Elevators(current_floor)
        last_request.set_order(++self.current_order)
        self.requests.append(last_request)

    def validate_floor(self, floor):
        if floor >= len(self.floors):
            raise ValueError("Invalid floor {}, this building only has {} floors.".format(floor, len(self.floors) - 1))

    def validate_direction(self, floor, direction):
        # At each floor — except the first one and the last one, the request can be made in two directions.
        if ((floor == 0) & (direction == -1)) | ((floor == len(self.floors)-1) & (direction == 1)):
            raise ValueError("Invalid direction {} for floor {}.".format(direction, floor))

    def validate_floor_elevator_direction(self, elevator, floor):
        # It is not possible to choose a floor that goes in the opposite direction of the outside call
        if ((elevator.direction == 1) & (floor < elevator.floor)) | ((elevator.direction == -1) & (floor > elevator.floor)):
            raise ValueError("Invalid floor {}, this elevator goes to the other direction.".format(floor))

    def move_elevator(self, elevator, to_floor):
        """Send elevator to floor, moving one floor at a time."""
        self.validate_floor(to_floor)
        if elevator.direction is not None:
            self.validate_floor_elevator_direction(elevator, to_floor)
        print("Elevator {} moving".format(elevator.id))
        elevator.set_direction(to_floor)

        for _ in (range(elevator.floor, to_floor)
        if elevator.direction == 1 else range(elevator.floor, to_floor, -1)):
            elevator.move(self)
            sleep(0.5)

        print("Elevator {} arrives to floor {}".format(elevator.id, to_floor))
        elevator.direction = None
        elevator.requests += 1

    def get_elevator(self, elevators, direction):
        # Get elevators travelling in the right direction
        my_elevators = [elevator for elevator in elevators if elevator.direction == direction]

        # If my_elevator is None, get default elevator
        if len(my_elevators) is 0:
            my_elevators = [elevator for elevator in elevators if elevator.default_elevator is True]

        my_elevators = sorted(my_elevators, key=lambda ele: ele.floor)
        for elevator in my_elevators:
            if elevator.requests <= len(self.floors)/len(self.elevators):
                return elevator
            else:
                raise ("Not elevator available", "All elevators have answer more than {} requests.")\
                    .format(len(self.floors)/len(self.elevators))


    def call_elevator(self, floor, direction):
        """Chooses and returns an elevator after moving it to floor.
        Floor should be the floor the elevator is called to.
        Direction should indicate which way the user wants to travel, values should be 1 or -1."""

        self.validate_floor(floor)
        self.validate_direction(floor, direction)
        if direction not in (1, -1):
            raise ValueError("direction only accepts 1 or -1, not {}".format(direction))

        #Check if there's any elevators on the current floor
        if self.floors[floor]:
            elevator = self.get_elevator(self.floors[floor], direction)
            print("<Elevator {} on floor {}>".format(len(self.floors), len(self.elevators)))
            return elevator
        # If not, look for an elevator in the rest of floors
        check_floors = []
        for elev in self.floors:
            for ele in elev:
                check_floors.append(ele)
        if check_floors is not None:
            elevator = self.get_elevator(check_floors, direction)
        else:
            raise Exception("Cannot find elevators.")

        self.move_elevator(elevator, floor)
        return elevator

