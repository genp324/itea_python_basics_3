<<<<<<< HEAD
from random import randint


class GameMap:

    def __init__(self, n, m, objects):

        self._n = n
        self._m = m
        self._map = self._generate_map()
        self._put_objects(objects)

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
=======
class GameMap:

    def __init__(self, n, m):

        self.n = n
        self.m = m
        self._generate_map()
>>>>>>> Added files 06

    def _generate_map(self):

        game_map = []

        for i in range(self._n):
            row = []
<<<<<<< HEAD
            
            for i in range(self._m):
                row.append(' ')
                
=======
            for i in range(self_m):
                row.append(' ')

    def _show_map(self):

        game_map = []

        for row in self._map:
            
            game_map.append('|')
            
            for i in row:

                game_map.append(f'{i}|')

            game_map.append('\n')

        game_map.pop()

        return ''.join(game_map)


if __name__ == '__main__':

    game_map = GameMap(5, 5)
    print(game_map)

