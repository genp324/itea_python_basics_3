traps_list = []
enemy_list = []
heal_list = []
check_list = []
exit_list = []

_KEYS = ('w','a','s','d')

def coords(obj,x,y):

    if str(obj) == 'Trap':
        traps_list.append([x, y])
        
    if str(obj) == 'Enemy':
        enemy_list.append([x, y])

    if str(obj) == 'Heal':
        heal_list.append([x, y])
    
    if str(obj) == 'Exit':
        exit_list.append([x, y])


def situations(x,y):

    if [x, y] in traps_list:
        traps_list.remove([x,y])

        return 'trap'

    elif  [x, y] in enemy_list:
        enemy_list.remove([x,y])

        return 'enemy'

    elif [x, y] in heal_list:
        heal_list.remove([x,y])

        return 'heal'

    elif [x, y] in exit_list:
        return 'exit'


def steps(step, x, y, cave_x, cave_y):

    if step not in _KEYS:
        print('Enter correct key!')
    
    elif step == 'w' and x > 1 :
        x -= 1

    elif step == 'a' and y > 1 :
        y -= 1

    elif step == 's' and x < cave_x  :
        x += 1

    elif step == 'd' and y < cave_y  :
        y += 1







    else:
        print('You kiss a Wall!')

    print (f'x: {x}  y: {y}')

    return x, y
