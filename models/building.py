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
        self.floors[1] = self.elevators[:]
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


    def move_elevator(self, elevator, to_floor):
       pass

    def get_elevator(self, elevators, direction):
       pass

    def validate_floor(self, floor):
        if floor >= len(self.floors):
            raise ValueError("Invalid floor {}, this building only "
                         "has {} floors.".format(floor, len(self.floors)))
        return True


    def call_elevator(self, floor, direction):
        """Chooses and returns an elevator after moving it to floor.
        Floor should be the floor the elevator is called to.
        Direction should indicate which way the user wants to travel, values should be 1 or -1."""

        self.validate_floor(floor)
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

