"""
Threat class
"""

class Threat:

    def __init__(self, position : tuple = (0, 0)):
        self._position = position
        self._isActive = False