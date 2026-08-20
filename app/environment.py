"""
Environment class for turn based FSM.

This module implements an Environment class for a Finite state machine.
"""

from random import randint
from typing import List
import time

class Environment:

    def __init__(self, width : int, height : int) -> None:
        self._grid = []
        for _ in range(height):
            temp = []
            for _ in range(width):
                temp.append(0)
            self._grid.append(temp)

        self._pheromoneGrid = self._grid[:]
        
        self._hive = {
            'position': (randint(0, height - 1), randint(0, width - 1)),
            'repr': 'H'
        }
        self._grid[self._hive['position'][0]][self._hive['position'][1]] = self._hive['repr']

        self._actors = []

    def query_cell(self, position : tuple) -> bool:
        y, x = position
        if y <= len(self._grid) or x <= len(self._grid[0]):
            if self._grid[y][x] == 0:
                return True
            return False
        return False

    def get_grid(self):
        return self._grid

    @property
    def grid(self) -> None:

        print('\033[H\033[J', end='') # Replace grid with new one for each environment update

        for row in self._grid:
            for _ in row:
                print(_, end=' ')
            print()
        time.sleep(2)

    def load_actors(self, actors : List[any]) -> None:

        for actor in actors:
            
            while not actor._isActive:
                new_position = (randint(0, len(self._grid) - 1), randint(0, len(self._grid[0]) - 1))

                if self._grid[new_position[0]][new_position[1]] == 0:
                    actor._position = new_position
                    self._grid[new_position[0]][new_position[1]] = actor
                    self._actors.append(actor)
                    actor._isActive = True

    def update(self):

        for row in self._grid:
            for cell in range(len(row)):
                row[cell] = 0

        self._grid[self._hive['position'][0]][self._hive['position'][1]] = self._hive['repr']

        for actor in self._actors:
            if actor._isActive:
                self._grid[actor._position[0]][actor._position[1]] = actor