from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS
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
    """
    This function takes 2 person character and enemy and serves the battle.
    :param character: character
    :param enemy: enemy
    :type character: str
    :type enemy: str
    :return: is_won
    :rtype: bool
    """
    is_won = True

    while True:

        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break

    return is_won


def move_one_step(toward):
    """
    This is a function witch take letter and convert it to increment coordinate on x, y.
    :param toward: string u - up,d - down,l - left,r - right
    :type toward: str
    :return: x, y

    """
    if toward == 'u':
        # up
        mv_x = -1
        mv_y = 0

    elif toward == 'd':
        # down
        mv_x = +1
        mv_y = 0

    elif toward == 'l':
        # left
        mv_x = 0
        mv_y = -1
    elif toward == 'r':
        # right
        mv_x = 0
        mv_y = 1
    else:
        mv_x = 0
        mv_y = 0
        print('Wrong key! Press this one (u, d, l, r)')

    return mv_x, mv_y


print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(5)]
    objects += enemies
elif level == 'Medium':
    objects = [choice(GAME_OBJECTS)() for i in range(2)]
    enemies = [choice(ENEMIES)() for i in range(3)]
    objects += enemies
elif level == 'Easy':
    objects = [choice(GAME_OBJECTS)() for i in range(2)]
    enemies = [choice(ENEMIES)() for i in range(1)]
    objects += enemies

x, y = randint(0, 5), randint(0, 5)
char = CHARACTERS[race](name, x, y)
char.show_stats()

map_dim_x = 8
map_dim_y = 8


game_map = GameMap(map_dim_x, map_dim_y, objects)
game_map.put_char(char, *char.get_coords())
count_enemy = game_map.get_count_enemy()
print(f'Left {count_enemy} enemies')
while True:

    print(game_map)
    old_x, old_y = char.get_coords()

    charkey = input('Move? left (l), right (r), up (u), down (d)')
    move_x, move_y = move_one_step(charkey)

    char.move_char(move_x, move_y)
    new_x, new_y = char.get_coords()

    if new_x < 0 or \
            new_y < 0 or \
            new_x >= map_dim_x or \
            new_y >= map_dim_y:
        print('You must move only inside map!')
        #  print(-move_x, -move_y)
        char.move_char(-move_x, -move_y)
        continue

    char2 = game_map.get_obj(new_x, new_y)
#    print(char2)
    name_on_map = game_map.get_name_on_map(new_x, new_y)
#    print(name_on_map)
    if char2 == ' ' or char2 is None:
        game_map.put_char(' ', old_x, old_y)
        game_map.put_char(char, new_x, new_y)
        continue

    elif char2 == '*' and name_on_map == 'Trap':
        get_trapped(char)

        if char.is_dead():
            game_map.put_char(' ', old_x, old_y)
            break
        else:
            game_map.put_char(' ', old_x, old_y)
            game_map.put_char(char, new_x, new_y)
            count_enemy -= 1
            print(f'Left {count_enemy} enemies')
            if count_enemy == 0:
                break

    elif char2 == '*' and name_on_map == 'Heal':
        get_healed(char)
        game_map.put_char(' ', old_x, old_y)
        game_map.put_char(char, new_x, new_y)

    elif char2 == '*' and name_on_map == 'Undead':
        print('ENEMY!!!')
        enemy = ENEMIES[0]()
        is_won = fight_with_enemy(char, enemy)

        if not is_won:
            game_map.put_char(' ', old_x, old_y)
            break
        else:
            game_map.put_char(' ', old_x, old_y)
            game_map.put_char(char, new_x, new_y)
            count_enemy -= 1
            print(f'Left {count_enemy} enemies')
            if count_enemy == 0:
                break

    elif char2 == '*' and name_on_map == 'Murloc':
        print('ENEMY!!!')
        enemy = ENEMIES[1]()
        is_won = fight_with_enemy(char, enemy)

        if not is_won:
            game_map.put_char(' ', old_x, old_y)
            break
        else:
            game_map.put_char(' ', old_x, old_y)
            game_map.put_char(char, new_x, new_y)
            count_enemy -= 1
            print(f'Left {count_enemy} enemies')
            if count_enemy == 0:
                break

    else:
        continue

if char.is_dead():
    print('Sorry, you lost.')
    print('Game Over')
else:
    print(f'You win !!! Your score: kill {game_map.get_count_enemy()} enemies and traps')
    print('Game Over')
