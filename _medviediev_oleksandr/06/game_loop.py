from random import randint, choice
from characters import CHARACTERS, ENEMIES


def get_trapped(character):

    print('You got trapped')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):

    print('You got healed')
    hp = randint(5, 25)
    character.get_healed(hp)


def fight_with_enemy(character, enemy):

    is_won = True

    while True:

        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break

    return is_won


print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    situations = ['trap', 'trap', 'trap', 'enemy', 'enemy', 'heal']
elif level == 'Medium':
    situations = ['trap', 'trap', 'enemy', 'heal']
elif level == 'Easy':
    situations = ['trap', 'enemy', 'heal', 'heal']

char = CHARACTERS[race](name)
char.show_stats()

while True:

    input('Move? ')
    situation = choice(situations)

    if situation == 'trap':
        
        get_trapped(char)
        if char.is_dead():
            break
        
    elif situation == 'heal':
        
        get_healed(char)
        
    elif situation == 'enemy':
        
        print('ENEMY!!!')
        enemy = choice(ENEMIES)()
        is_won = fight_with_enemy(char, enemy)

        if not is_won:
            break

print('Sorry, you lost.')
print('Game Over')

    
