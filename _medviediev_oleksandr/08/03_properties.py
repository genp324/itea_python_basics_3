class Character:

    def __init__(self, name):

        self._name = name
        self._hp = 90
        self._damage = 10

    @property
    def hp(self):
        return f'HP: {self._hp}'

    @hp.setter
    def hp(self, new_hp):
        if self._hp + new_hp >= 100:
            self._hp = 100
        else:
            self._hp = new_hp


char = Character('Name')
print(char.hp)
char.hp = 120
print(char.hp)
