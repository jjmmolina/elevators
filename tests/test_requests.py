# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 27/05/2020

"""
import random
import threading
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

    def test_validate_floor_elevator_direction(self):
        to_floor = 3
        elevator = self.building.elevators[0]
        elevator.floor = 4
        elevator.direction = 1
        self.assertRaises(ValueError, self.building.validate_floor_elevator_direction,elevator, to_floor)
        to_floor = 5
        self.assertEqual(None, self.building.validate_floor_elevator_direction(elevator, to_floor))

    def test_validate_direction(self):
        from_floor = 0
        direction = -1
        self.assertRaises(ValueError, self.building.validate_direction, from_floor, direction)
        direction = 1
        self.assertEqual(None, self.building.validate_direction(from_floor, direction))
        from_floor = 5
        self.assertRaises(ValueError, self.building.validate_direction, from_floor, direction)
        direction = -1
        self.assertEqual(None, self.building.validate_direction(from_floor, direction))

    def test_add_request_elevators(self):
        from_floor = 4
        to_floor = 5
        self.building.add_request(from_floor, to_floor)
        self.assertEqual(1, len(self.building.requests))
        from_floor = 4
        to_floor = 1
        self.building.add_request(from_floor, to_floor)
        self.assertEqual(2, len(self.building.requests))
        from_floor = 3
        to_floor = 4
        self.building.add_request(from_floor, to_floor)
        self.assertEqual(3, len(self.building.requests))

    def test_move_passengers_sequentially(self):
        for _ in range(10):
            from_floor, to_floor = random.sample(range(len(self.building.floors)), 2)
            request = Requests_Elevators(from_floor, to_floor)
            print(request.__str__())
            self.building.requests.append(request)
        self.building.requests = sorted(self.building.requests, key=lambda request: request.current_floor)
        for request in self.building.requests:
            self.building.move_passengers(request.current_floor, request.next_floor)

        self.assertEqual(0, len(self.building.requests))
    def test_move_passengers(self):
        for _ in range(6):
            from_floor, to_floor = random.sample(range(len(self.building.floors)), 2)
            request = Requests_Elevators(from_floor, to_floor)
            print(request.__str__())
            self.building.requests.append(request)
        self.building.requests = sorted(self.building.requests, key=lambda request: request.current_floor)
        for request in self.building.requests:
            # t = threading.Thread(target=self.building.move_passengers, args=(request.current_floor, request.next_floor))
            # t.start()
            self.building.move_passengers(request.current_floor, request.next_floor)
        self.assertEqual(0, len(self.building.requests))

    def test_move_passenger_demo(self):
        from_floor = 0
        to_floor = 4
        self.building.add_request(from_floor, to_floor)
        from_floor = 0
        to_floor = 4
        self.building.add_request(from_floor, to_floor)
        from_floor = 0
        to_floor = 4
        self.building.add_request(from_floor, to_floor)
        from_floor = 0
        to_floor = 3
        self.building.add_request(from_floor, to_floor)
        from_floor = 4
        to_floor = 0
        self.building.add_request(from_floor, to_floor)
        from_floor = 2
        to_floor = 3
        self.building.add_request(from_floor, to_floor)
        from_floor = 2
        to_floor = 3
        self.building.add_request(from_floor, to_floor)
        self.building.requests = sorted(self.building.requests, key=lambda request: request.current_floor)

        self.building.move_passengers()
        self.assertEqual(0, len(self.building.requests))

    def tearDown(self):
        self.building = None
