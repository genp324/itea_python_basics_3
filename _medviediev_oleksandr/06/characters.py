class Character:

    _initial_hp = 100

    def __init__(self, name):

        self._name = name
        self._assign_stats()

    def _assign_stats(self): 
    
        self._hp = 100
        self._damage = 10
        self._race = None

    def show_stats(self):

        print('Character stats: ')
        print(f'Name: {self._name}')
        print(f'HP: {self._hp}')
        print(f'Damage: {self._damage}')
        print(f'Race: {self._race}')

    def get_damaged(self, damage):

        print(f'{self._name} get damaged by {damage}')
        self._hp -= damage
        print(f'{self._hp} left')

    def get_healed(self, hp):

        print(f'{self._name} get healed by {hp}')
        
        approximate_hp = self._hp + hp

        if approximate_hp >= self._initial_hp:
            self._hp = self._initial_hp
        else:
            self._hp = approximate_hp
            
        print(f'{self._hp} left')


class Human(Character):

    _initial_hp = 100

    def _assign_stats(self):

        self._hp = self._initial_hp
        self._damage = 10
        self._race = 'Human'
    
class Orc(Character):

    _initial_hp = 120

    def _assign_stats(self):

        self._hp = self._initial_hp
        self._damage = 15
        self._race = 'Orc'


class Elf(Character):

    _initial_hp = 90

    def _assign_stats(self):

        self._hp = self._initial_hp
        self._damage = 20
        self._race = 'Elf'


CHARACTERS = {'Human': Human, 'Orc': Orc, 'Elf': Elf}

