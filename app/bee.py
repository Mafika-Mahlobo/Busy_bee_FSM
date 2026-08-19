"""
Bee class

This module defines a bee agent
"""

STATES = {
     'wondering': 1,
     'foraging': 2,
     'attacking': 3,
     'to_hive': 4
}

class Bee:

    _id = 0
     
    def __init__(self, health : int = 100, energy : int = 100, pollen : int = 0, position : tuple = (0, 0), state : int = 1) -> None:
        self._health = health
        self._energy = energy
        self._pollen = pollen
        self._position = position
        self._state = state
        self._isActive = False
        self._id = Bee._id
        Bee._id += 1
       

    def __repr__(self) -> int:
        return f'B{self._id}'

    def update(self):
        pass