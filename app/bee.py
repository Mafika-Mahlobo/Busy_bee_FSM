"""
Bee class

This module defines a bee agent
"""

from app.flower import Flower
from app.threat import Threat

STATES = {
     'wondering': 1,
     'foraging': 2,
     'attacking': 3,
     'to_hive': 4,
     'die': 5
}

MAX_POLLEN_STRENGTH = 10

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
        self._direction = 1
        Bee._id += 1
        self._environment = environment
       

    def __repr__(self) -> int:
        return f'B{self._id}'

    def attacking(self, threat : Threat) -> None:
            threat._isActive = False
            self._position = (threat._position[0], threat._position[1])
            self._environment._pheromoneGrid[threat._position[0]][threat._position[1]] = MAX_POLLEN_STRENGTH
            self._state = STATES['wondering']

    def navigate_fwd(self):
        current_row = self._environment.get_grid()[self._position[0]]
        for index in range(self._position[1], len(current_row)):
            cell = current_row[index]
            if cell == 0:
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Flower):
                self._pollen += 1
                self._state = STATES['to_hive']
                cell._isActive = False
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Threat):
                self._state = STATES['attacking']
                self.attacking(cell)
                break
        else:
            next_row = self._position[0] + 1
            if next_row < len(self._environment.get_grid()):
                next_cell = self._environment.get_grid()[next_row][0]
                if next_cell == 0:
                    self._position = (next_row, 0)
                elif isinstance(next_cell, Flower):
                    self._pollen += 1
                    self._state = STATES['to_hive']
                    next_cell._isActive = False
                    self._position = (next_row, 0)
                elif isinstance(next_cell, Threat):
                    self._state = STATES['attacking']
                    self.attacking(next_cell)
                    

    def navigate_bck(self):
        current_row = self._environment.get_grid()[self._position[0]]
        for index in range(self._position[1], -1, -1):
            cell = current_row[index]
            if cell == 0:
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Flower):
                self._state = STATES['to_hive']
                cell._isActive = False
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Threat):
                self._state = STATES['attacking']
                self.attacking(cell)
                break
        else:
            previous_row = self._position[0] - 1
            if previous_row >= 0:
                previous_cell = self._environment.get_grid()[previous_row][-1]
                if previous_cell == 0:
                    self._position = (previous_row, len(current_row) - 1)
                elif isinstance(previous_cell, Flower):
                    self._pollen += 1
                    self._state = STATES['to_hive']
                    previous_cell._isActive = False
                    self._position = (previous_row, len(current_row) - 1)
                elif isinstance(previous_cell, Threat):
                    self._state = STATES['attacking']
                    self.attacking(previous_cell)
             
                    

    def wondering(self):
        current_row = self._environment.get_grid()[self._position[0]]

        for index in range(len(current_row)):
            if isinstance(current_row[index], Flower):

                if index < self._position[1]:
                    self._direction = -1
                    break
                else:
                    self._direction = 1
                    break
    
        if self._position[0] == len(self._environment._grid) and self._position[1] == len(current_row):
            self._direction = -1

        elif self._position[0] == 0 and self._position[1] == 0:
            self._direction = 1

        if self._direction == 1:
            self.navigate_fwd()
        else:
            self.navigate_bck()

    def foraging(self):
        pass

    def return_to_hive(self):
        pass

    def die(self):
        self._isActive = False

    def hive_management(self):
        pass


    def update(self):

        match self._state:
            case 1:
                self.wondering()

            case 2:
                self.foraging()

            case 3:
                self.attacking()

            case 4:
                self.return_to_hive()

            case 5:
                self.die()                                      