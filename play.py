# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 28/05/2020

"""
import click
import random
from random import sample
from time import sleep
from models.building import Building
from models.requests_elevators import Requests_Elevators


class Play:
    """This class is used to run the elevator's simulator."""
    def __init__(self, floors, elevators, requests):
        self.floors = floors
        self.elevators = elevators
        self.requests = requests
        self.building = Building(self.floors, self.elevators)

    def generate_requests(self):
        from_floor, to_floor = random.sample(range(self.floors), 2)
        request = Requests_Elevators(from_floor, to_floor)
        print(request.__str__())
        self.building.requests.append(request)

    def run(self):
        """This method is used to start. """
        print(self.building.__repr__())
        print(self.building.__str__())

        self.building.move_passengers()
        while True:
            self.generate_requests()
            sleep(5)



@click.command()
@click.option('--floors', '-f', default=10, help='The number of floors in the building')
@click.option('--elevators', '-e', default=5, help='The number of elevators working ind the building')
@click.option('--requests', '-r', default=5, help='Number of simulated requests to run the application')
def play(floors, elevators, requests):
    """Starts a simulation of the game"""
    playing = Play(floors, elevators, requests)
    playing.run()




if __name__ == '__main__':
    play()