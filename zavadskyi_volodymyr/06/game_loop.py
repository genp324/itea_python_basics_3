from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS, FINAL
from game_map import GameMap


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
    objects = [choice(GAME_OBJECTS)() for i in range(5)]
    objects += [choice(ENEMIES)() for i in range(5)]
    objects += [choice(FINAL)() for i in range(1)]
elif level == 'Medium':
    objects = [choice(GAME_OBJECTS)() for i in range(5)]
    objects += [choice(ENEMIES)() for i in range(4)]
    objects += [choice(FINAL)() for i in range(1)]
elif level == 'Easy':
    objects = [choice(GAME_OBJECTS)() for i in range(5)]
    objects += [choice(ENEMIES)() for i in range(3)]
    objects += [choice(FINAL)() for i in range(2)]

x, y = randint(0, 4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

map_measure = int(input('Choose the measure of map? '))

game_map = GameMap(map_measure, map_measure, objects)
game_map.put_char(char, *char.get_coords())

while True:
     
    print(game_map)
    
    step = input('Move? ')
    
    if step == 'up':
        move = (-1, 0)
    elif step == 'down':
        move = (1, 0)
    elif step == 'left':
        move = (0, -1)
    elif step == 'right':
        move = (0, 1)
    
    cur = char.get_coords()
    next_p = tuple(map(lambda a, b: a + b, cur, move))
    print(next_p)

    if not (next_p[0] >= 0 and next_p[1] >= 0 and next_p[0] <= map_measure - 1 and next_p[1] <= map_measure - 1):
            print ("You was killed by the wall! Stay on map!")
            break
        
    for element in objects:
        if element.backup()[0] == next_p:
            situation = element.backup()[1]
        
        else:
            situation = 'Nothing'
        
        if situation == 'Trap':
            
            get_trapped(char)
            if char.is_dead():
                print('You lost!')
                break
            
        elif situation == 'Heal':
            
            get_healed(char)
            
        elif situation == 'Undead' or situation == 'Murloc':
            
            print('ENEMY!!!')
            enemy = choice(ENEMIES)()
            is_won = fight_with_enemy(char, enemy)

            if not is_won:
                print('You lost!')
                break
            
        elif situation == 'Final':

            print('You won!')
            break

    char.moving(move)
    new_coords = char.get_coords()
    game_map.move_char(char, *cur, *new_coords)

print('Game Over')
