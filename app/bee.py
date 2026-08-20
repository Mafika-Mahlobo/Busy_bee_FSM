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

MAX_PHEROMONE_STRENGTH = 10

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

    def foraging(self):
        self._pollen += 1
        Threat = self._environment.get_grid()[self._position[0]][self._position[1]]
        Threat._isActive = False
        self._state = STATES['to_hive']

    def attacking(self) -> None:
        self._health -= 10
        threat = self._environment.get_grid()[self._position[0]][self._position[1]]
        threat._isActive = False
        self._environment._pheromoneGrid[threat._position[0]][threat._position[1]] = MAX_PHEROMONE_STRENGTH
        self._state = STATES['wondering']

    def deposit_pollen(self):
        self._pollen = 0
        self._health = 100
        self._environment._hive['pollen_count'] += 1
        self._environment._hive['repr'] = f"H{self._environment._hive['pollen_count']}"


    def return_to_hive(self):
        hive_position = self._environment._hive['position']

        if self._position == hive_position:
            self.deposit_pollen()
            self._state = STATES['wondering']
            return

        current_index = self._position[0] * len(self._environment.get_grid()[0]) + self._position[1]
        hive_index = hive_position[0] * len(self._environment.get_grid()[0]) + hive_position[1]
        self._direction = 1 if current_index < hive_index else -1
        
        if self._direction == 1:
            self.navigate_fwd()
        else:
            self.navigate_bck()


    def navigate_fwd(self):
        current_row = self._environment.get_grid()[self._position[0]]
        for index in range(self._position[1], len(current_row)):
            cell = current_row[index]
            if cell == 0:
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Bee):
                continue

            elif isinstance(cell, Flower):
                self._position = (cell._position[0], cell._position[1])
                self._state = STATES['foraging']
                self.foraging()

            elif isinstance(cell, Threat):
                self._position = (cell._position[0], cell._position[1])
                self._state = STATES['attacking']
                self.attacking()
                break

            elif isinstance(cell, str) and cell.startswith('H'):
                if self._pollen > 0:
                    self.deposit_pollen()
                self._state = STATES['wondering']

        else:
            next_row = self._position[0] + 1
            if next_row < len(self._environment.get_grid()):
                next_cell = self._environment.get_grid()[next_row][0]
                if next_cell == 0:
                    self._position = (next_row, 0)

                elif isinstance(next_cell, Bee):
                    if len(current_row) > 1:
                        self._position = (next_row, 1)
                    else:
                        self._direction = -1

                elif isinstance(next_cell, Flower):
                    self._position = (next_cell._position[0], next_cell._position[1])
                    self._state = STATES['foraging']
                    self.foraging()
                    
                    
                elif isinstance(next_cell, Threat):
                    self._position = (next_cell._position[0], next_cell._position[1])
                    self._state = STATES['attacking']
                    self.attacking()

                elif isinstance(next_cell, str) and next_cell.startswith('H'):
                    if self._pollen > 0:
                        self.deposit_pollen()
                    self._state = STATES['wondering']
                    if len(current_row) > 1:
                        self._position = (next_row, 1)
                    else:
                        self._direction = -1
                    
            else:
                self._direction = -1
                    

    def navigate_bck(self):
        current_row = self._environment.get_grid()[self._position[0]]
        for index in range(self._position[1], -1, -1):
            cell = current_row[index]
            if cell == 0:
                self._position = (self._position[0], index)
                break
            elif isinstance(cell, Bee):
                continue

            elif isinstance(cell, Flower):
                self._position = (cell._position[0], cell._position[1])
                self._state = STATES['foraging']
                self.foraging()
                
            elif isinstance(cell, Threat):
                self._position = (cell._position[0], cell._position[1])
                self._state = STATES['attacking']
                self.attacking()
                break

            elif isinstance(cell, str) and cell.startswith('H'):
                if self._pollen > 0:
                    self.deposit_pollen()
                self._state = STATES['wondering']
        else:
            previous_row = self._position[0] - 1
            if previous_row >= 0:

                previous_cell = self._environment.get_grid()[previous_row][-1]

                if previous_cell == 0:
                    self._position = (previous_row, len(current_row) - 1)

                elif isinstance(previous_cell, Bee):
                    if len(current_row) > 1:
                        self._position = (previous_row, len(current_row) - 2)
                    else:
                        self._direction = 1

                elif isinstance(previous_cell, Flower):
                    self._position = (previous_cell._position[0], previous_cell._position[1])
                    self._state = STATES['foraging']
                    self.foraging()
                   

                elif isinstance(previous_cell, Threat):
                    self._position = (previous_cell._position[0], previous_cell._position[1])
                    self._state = STATES['attacking']
                    self.attacking()
                    
                elif isinstance(previous_cell, str) and previous_cell.startswith('H'):
                    if self._pollen > 0:
                        self.deposit_pollen()
                    self._state = STATES['wondering']
                    if len(current_row) > 1:
                        self._position = (previous_row, len(current_row) - 2)
                    else:
                        self._direction = 1
            else:
                self._direction = 1
             
                    

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
    
        if (self._position[0] == len(self._environment._grid) - 1 and self._position[1] == len(current_row) - 1):
            self._direction = -1

        elif self._position[0] == 0 and self._position[1] == 0:
            self._direction = 1

        if self._direction == 1:
            self._energy -= 1
            self.navigate_fwd()
        else:
            self._energy -= 1
            self.navigate_bck()


    def die(self):
        self._isActive = False

    def update(self):

        if self._health < 1 or self._energy < 1:
            self._state = STATES['die']

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