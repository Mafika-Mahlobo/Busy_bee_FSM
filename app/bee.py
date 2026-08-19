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

    id = -1
     
    def __init__(self, health : int = 100, energy : int = 100, pollen : int = 0, position : tuple = (0, 0), state : int = 1):
        self._health = health
        self._energy = energy
        self._pollen = pollen
        self._position = position
        self._state = state
        self._isActive = False
        Bee.id += 1
        self._id = id
       

    def __repr__(self):
        return f'B - {self._id}'

    def update(self):
        pass