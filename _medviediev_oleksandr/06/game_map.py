from random import randint


class GameMap:

    def __init__(self, n, m, objects=None):

        self._n = 8
        self._m = 8
        self._map = self._generate_map()
        # self._put_objects(objects)

    def __str__(self):

        game_map = self._show_map()
        return game_map

    def _put_objects(self, objects):

        for obj in objects:
            x = randint(0, self._n - 1)
            y = randint(0, self._m - 1)
            self._map[x][y] = str(obj)

    def put_char(self, char, x, y):
        self._map[x][y] = str(char)

    def _generate_map(self):

        game_map = []

        for i in range(self._n):
            row = []
            
            for i in range(self._m):
                row.append(' ')
                
            game_map.append(row)

        return game_map

    def _show_map(self):

        game_map = []

        game_map.append('    A B C D E F G H\n\n')

        for index, row in enumerate(self._map):
            
            game_map.append(f'{index + 1}  |')
            
            for i in row:

                game_map.append(f'{i}|')

            game_map.append(f'  {index + 1}\n')

        game_map.append('\n    A B C D E F G H')

        return ''.join(game_map)


if __name__ == '__main__':

    game_map = GameMap(5, 5)
    print(game_map)
