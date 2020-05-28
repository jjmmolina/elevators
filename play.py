# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 28/05/2020

"""
import click
from models.building import Building


class Play:
    """This class is used to run the elevator's simulator."""
    def __init__(self, floors, elevators):
        self.floors = floors
        self.elevators = elevators

    def run(self):
        """This method is used to start. """
        building = Building(self.floors, self.elevators)
        print(building.__repr__())
        print(building.__str__())


@click.command()
@click.option('--floors', '-f', default=10, help='The number of floors in the building')
@click.option('--elevators', '-e', default=5, help='The number of elevators working ind the building')
def play(floors, elevators):
    """Starts a simulation of the game"""
    playing = Play(floors, elevators)
    playing.run()


if __name__ == '__main__':
    play()