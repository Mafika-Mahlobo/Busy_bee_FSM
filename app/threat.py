"""
Threat class
"""

class Threat:

    _id = 0

    def __init__(self, position : tuple = (0, 0)):
        self._position = position
        self._id = Threat._id
        Threat._id += 1
        self._isActive = False

    def __repr__(self) -> int:
        return f'T{self._id}'