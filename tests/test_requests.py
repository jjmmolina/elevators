# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""

import unittest

from models.building import Building
from models.elevators import Elevator
from models.requests_elevators import Requests_Elevators


# class ElevatorsTestCase(unittest.TestCase):
#     my_elevator = Elevator(1)
#
#     def setUp(self):
#         self.my_elevator.direction = 1
#
#
#     def test_first_floor(self):
#         next_floor = 2
#         self.assertEqual(1, self.my_elevator.got_to_up(next_floor))
#         self.assertEqual(False, self.my_elevator.got_to_down(next_floor))
#
#     def test_last_floor(self, floor):
#         self.assertEqual(True, self.my_elevator.go_to_down(floor))
#         self.assertEqual(False, self.my_elevator.go_to_up(floor))
#
#     def test_default_elevator(self):
#         self.assertEqual(True, self.my_elevator.is_default_elevator())
#
#     def test_my_direction(self, direction):
#         self.assertTrue(Elevator.is_my_direction(direction))
#
#     def test_move(self, from_floor, to_floor):
#         self.assertEqual(True, Building.move_elevator(from_floor, to_floor))
#         pass
#     def test_max_request(self):
#         pass
#     def tearDown(self):
#         pass

class BuildingTestCase(unittest.TestCase):
    building = None

    def setUp(self):
        self.building = Building(5, 3)

    def test_get_elevator(self):
        direction = 1
        self.assertIsInstance(self.building.get_elevator(self.building.elevators, direction), Elevator)
        direction = -1
        self.assertIsInstance(self.building.get_elevator(self.building.elevators, direction), Elevator)

    def test_call_elevator(self):
        from_floor = 3
        direction = 1
        # Nearest elevator arrives to floor 'from_floor"
        self.assertIsInstance(self.building.call_elevator(from_floor, direction), Elevator)

    def test_move_elevator(self):
        to_floor = 5
        elevator = self.building.elevators[0]
        self.building.move_elevator(elevator, to_floor)
        self.assertEqual(to_floor, elevator.floor)
        to_floor = 6
        self.assertRaises(ValueError, self.building.move_elevator, elevator, to_floor)


    def tearDown(self):
        pass
