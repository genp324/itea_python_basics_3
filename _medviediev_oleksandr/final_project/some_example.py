from random import choice


class Checker:

    def __init__(self, x, y, color):

        self.name = f'{x}{y}'
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return self.color


white_army = [Checker(0, 1, 'X'), Checker(0, 3, 'X')]

game_map = [[' ', 'X', ' ', ' ', ' '],
            [' ', ' ', 'O', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']]

possible_moves = {}

for checker in white_army:

    game_map[checker.x][checker.y] = checker

    if game_map[checker.x + 1][checker.y - 1] == ' ':
        possible_moves[checker.name] = [(checker.x + 1, checker.y - 1)]
    if game_map[checker.x + 1][checker.y + 1] == ' ':
        possible_moves[checker.name].append((checker.x + 1, checker.y + 1))

print(possible_moves)
checker_to_move = choice(list(possible_moves.keys()))
print(checker_to_move)
coords_to_move = choice(possible_moves[checker_to_move])
print(coords_to_move)




