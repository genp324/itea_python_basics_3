from random import randint, choice
from characters import CHARACTERS


def get_trapped(character):

    print('You got trapped')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):

    print('You got healed')
    hp = randint(5, 25)
    character.get_healed(hp)


print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')

char = CHARACTERS[race](name)
char.show_stats()

situations = ['trap', 'trap', 'heal']

while True:

    input('Move? ')
    situation = choice(situations)

    if situation == 'trap':
        get_trapped(char)
    elif situation == 'heal':
        get_healed(char)

    
    

    
