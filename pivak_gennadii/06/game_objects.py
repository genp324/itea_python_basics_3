class Magic:

    def __str__(self):
        return '*'

    def get_name(self):
        return self._name


class Trap(Magic):

    def __init__(self):
        self._name = 'Trap'


class Heal(Magic):

    def __init__(self):
        self._name = 'Heal'


GAME_OBJECTS = [Trap, Heal]
