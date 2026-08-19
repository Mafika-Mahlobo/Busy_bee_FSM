"""
Bee class

This module defines a bee agent
"""

from app.environment import Environment

STATES = {
     'wondering': 1,
     'foraging': 2,
     'attacking': 3,
     'to_hive': 4
}

class Bee:

    _id = 0
     
    def __init__(self, health : int = 100, energy : int = 100, pollen : int = 0, position : tuple = (0, 0), state : int = 1, environment = None) -> None:
        self._health = health
        self._energy = energy
        self._pollen = pollen
        self._position = position
        self._state = state
        self._isActive = False
        self._id = Bee._id
        Bee._id += 1
        self._environment = environment
       

    def __repr__(self) -> int:
        return f'B{self._id}'
    

    def update(self):

        match self._state:
            case 1:
                is_empty = False
                x_forward = (self._position[0], self._position[1] + 1)
                x_back = (self._position[0], self._position[1] - 1)
                y_up = (self._position[0] - 1, self._position[1])
                y_down = (self._position[0] + 1, self._position[1])
                
                while not is_empty:
                    is_empty = self._environment.query_cell(x_forward)
                    if not is_empty:
                        is_empty = self._environment.query_cell(x_back)
                        if not is_empty:
                            is_empty = self._environment.query_cell(y_up)
                            if not is_empty:
                                is_empty = self._environment.query_cell(y_down)


            case 2:
                pass

            case 3:
                pass

            case 4:
                pass