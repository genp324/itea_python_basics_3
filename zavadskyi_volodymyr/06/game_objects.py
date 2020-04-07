class Object:


    def coords(self, x, y):

        self._x = x
        self._y = y


    def get_coords(self):

        return self._x, self._y

    def backup(self):
        backup = [(self._x, self._y), self._name]
        return backup


class Trap(Object):

    def __init__(self):
        self._name = 'Trap'

    def __str__(self):
        return '*'


class Heal(Object):

    def __init__(self):
        self._name = 'Heal'

    def __str__(self):
        return '*'

class Final(Object):
    
    def __init__(self):
        self._name = 'Final'

    def __str__(self):
        return '*'


FINAL = [Final]
GAME_OBJECTS = [Trap, Heal]
