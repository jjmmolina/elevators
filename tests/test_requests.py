# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""

import unittest

from models.building import Building
from models.elevators import Elevator
from models.floors import Floor
from models.requests_elevators import Requests_Elevators


class ElevatorsTestCase(unittest.TestCase):
    my_elevator = Elevator()

    def setUp(self):
        self.my_elevator.direction = 1
        pass
        

    def test_first_floor(self, floor):
        self.assertEqual(True, self.my_elevator.go_to_up(floor))
        self.assertEqual(False, self.my_elevator.go_to_down(floor))

    def test_last_floor(self, floor):
        self.assertEqual(True, self.my_elevator.go_to_down(floor))
        self.assertEqual(False, self.my_elevator.go_to_up(floor))

    def test_default_elevator(self):
        self.assertEqual(True, self.my_elevator.is_default_elevator())
        
    def test_my_direction(self, direction):
        self.assertTrue(Elevator.is_my_direction(direction))

    def test_max_request(self):
        pass

    def tearDown(self):
        pass

class FloorsTestCase(unittest.TestCase):
    floor_1 = Floor()
    floor_NoN = Floor()


    def setUp(self):
        self.floor_1.number = 1
        self.floor_NoN.number = 0
        pass

    def test_available_floor(self):
        self.assertEqual(True, self.floor.number)
        self.assertEqual(False, self.floor_NoN.number)

    def tearDown(self):
        pass

class RequestsTestCase(unittest.TestCase):
    elevators = []
    floors = []

    elevator_1 = Elevator()
    elevator_2 = Elevator()
    elevators.append(elevator_1)
    elevators.append(elevator_2)

    floor_1 = Floor()
    floor_2 = Floor()
    floor_3 = Floor()
    floors.append(floor_1)
    floors.append(floor_2)
    floors.append(floor_3)

    building = Building(floors, elevators)
    request = Requests_Elevators()

    def setUp(self):
        self.elevator_1.direction = 1
        self.elevator_2.direction = 0
        pass

    def test_available_elevator(self):
        self.assertEqual(True, self.building.is_available_elevator())


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
