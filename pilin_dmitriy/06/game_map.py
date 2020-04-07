from random import randint
import move


class GameMap:

    def __init__(self, n, m, objects):

        self._n = n + 1
        self._m = m + 1
        self._map = self._generate_map()
        self._put_objects(objects)


    def __str__(self):

        game_map = self._show_map()
        return game_map


    def _put_objects(self, objects):

        coord_list = []
        self._put_exit_door()
        
        for obj in objects:

            x = randint(1, self._n - 1)
            y = randint(1, self._m - 1)

            while True:

                if [x, y] not in coord_list:
                    break
                
                x = randint(1, self._n - 1)
                y = randint(1, self._m - 1)

            move.coords(obj, x, y)
            coord_list = move.heal_list + move.traps_list + move.enemy_list + move.exit_list

        for i in coord_list:

            x,y = i
            self._map[x][y] = '*'


    def _put_exit_door(self):

        x = randint(1, self._n - 1)
        y = randint(1, self._m - 1)

        move.coords('Exit', x, y)
    

    def put_char(self, char, x, y):
        self._map[x][y] = str(char)

    def clear_step(self, x, y):
        self._map[x][y] = ' '

    def _generate_map(self):

        game_map = []
        _num_x = 0
        _num_y = 1
        for i in range(self._n):
            row = []
            
            for j in range(self._m):
                if i == 0 :
                    row.append(_num_x)
                    _num_x +=1
                elif j == 0:
                    row.append(_num_y)
                    _num_y +=1
                else:
                    row.append(' ')
                
            game_map.append(row)

        return game_map

    def _show_map(self):

        game_map = []

        for row in self._map:
            
            game_map.append('|')
            
            for i in row:

                game_map.append(f'{i}|')

            game_map.append('\n')

        game_map.pop()

        return ''.join(game_map)
    