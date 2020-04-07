from random import randint


class GameMap:

    def __init__(self, n, m, objects):

        self._n = n
        self._m = m
        self._count_enemy = 0
        self._map = self._generate_map()
        self._name = self._generate_map()  # create hidden layer map
        self._put_objects(objects)

    def __str__(self):

        game_map = self._show_map()
        return game_map

    def _put_objects(self, objects):
        """
        This is a function witch put objects on map and count enemies.
        :param objects: list of objects
        :type objects: list
        """
        for obj in objects:
            x = randint(0, self._n - 1)
            y = randint(0, self._m - 1)
            self._map[x][y] = str(obj)

            obj_name = obj.get_name()
            print(obj_name)
            self._name[x][y] = obj_name

            if obj_name in ('Trap', 'Undead', 'Murloc'):
                self._count_enemy += 1

    def put_char(self, char, x, y):
        """
        This is a function witch put Character on map.
        :param char: string
        :param x: coordinate x
        :param y: coordinate y
        :type char: object
        :type x: int
        :type y: int
        """
        self._map[x][y] = str(char)

    def get_obj(self, x, y):
        """
        This is a function witch get symbol (*) from map by coordinate x, y.
        :param x: coordinate x
        :param y: coordinate y
        :type x: int
        :type y: int
        """
        obj = self._map[x][y]

        return obj

    def get_name_on_map(self, x, y):
        """
        This is a function witch get Name object from hidden map by coordinate x, y.
        :param x: coordinate x
        :param y: coordinate y
        :type x: int
        :type y: int
        """
        obj = self._name[x][y]

        return obj

    def get_count_enemy(self):
        """
        This is a function witch return count of enemies from map.
        """
        return self._count_enemy

    def _generate_map(self):

        game_map = [[' ' for i in range(self._m)] for i in range(self._n)]
        '''
        game_map = []

        for i in range(self._n):
            row = []

            for i in range(self._m):
                row.append(' ')

            game_map.append(row)
        '''
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


if __name__ == '__main__':

    objects = [Trap(), Undead(), Undead(), Heal()]
    game_map = GameMap(6, 6, objects)
    print(game_map)
