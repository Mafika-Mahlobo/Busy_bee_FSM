"""
Flower class
"""

class Flower:

    _id = 0

    def __init__(self, position : tuple = (0, 0)) -> None:
        self._position = position
        self._id = Flower._id
        Flower._id += 1
        self._pollen = 5
        self._isActive = False

    def __repr__(self):
        return f'F{self._id}'