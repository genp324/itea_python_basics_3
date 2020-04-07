from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS
from game_map import GameMap
import move


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
# name = input('Enter your name: ')
name = 'Test'
# race = input('Choose race [Human, Orc, Elf]: ')
race = 'Orc'
# level = input('Difficulty [Hard, Medium, Easy]: ')
level = 'Hard'

cave_x = 8
cave_y = 8

if level == 'Hard':

    objects = [choice(GAME_OBJECTS)() for i in range(6)]
    enemies = [choice(ENEMIES)() for i in range(15)]
    
    objects += enemies

     
elif level == 'Medium':

    objects = [choice(GAME_OBJECTS)() for i in range(4)]
    enemies = [choice(ENEMIES)() for i in range(6)]

    objects += enemies


elif level == 'Easy':

    objects = [choice(GAME_OBJECTS)() for i in range(7)]
    enemies = [choice(ENEMIES)() for i in range(4)]

    objects += enemies

x, y = randint(1, cave_x), randint(1, cave_y)
char = CHARACTERS[race](name, x, y)
char.show_stats()

player_x,player_y = char.get_coords()

game_map = GameMap(cave_x, cave_y, objects)
game_map.put_char(char, *char.get_coords())

print(f'Traps: {move.traps_list}')
print(f'Enemy: {move.enemy_list}')
print(f'Heal: {move.heal_list}')
print(f'Exit: {move.exit_list}')
print(f'Player:[{player_x}, {player_y}]')


while True:
    print(game_map)

    step = input('Move? w,a,s,d\n')

    game_map.clear_step(player_x, player_y)
 
    player_x, player_y = move.steps(step, player_x, player_y, cave_x, cave_y)
    game_map.put_char(char, player_x, player_y)
    
    situation = move.situations(player_x, player_y)

    if situation == 'trap':
        
        get_trapped(char)

        if char.is_dead():

            print('Sorry, you lost.\nGame Over')
            break
        
    elif situation == 'heal':
        get_healed(char)
        
    elif situation == 'enemy':
        
        print('ENEMY!!!')
        enemy = choice(ENEMIES)()
        is_won = fight_with_enemy(char, enemy)

        if not is_won:

            print('Sorry, you lost.\nGame Over')
            break

    elif situation == 'exit':

        print('YOU FOUND EXIT AND WON!')
        break

        

 


    
