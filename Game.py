from Board import Board
from Player import Player


def input_(msg):
    while True:
        try:
            y, x = input(msg).strip().split()
            if not y.isdigit() or not x.isdigit():
                print('Need two positive numbers like: 0 0')
                continue
        except ValueError as e:
            print('ValueError: not enough values to unpack')
            continue
        return y, x


class Game:
    def __init__(self, board: Board, players: [Player]):
        self.board: Board = board
        self.players: [Player] = players

    def start(self):
        self.board.show()
        game_over = False
        while not game_over:
            for player in self.players:
                print(player.name + ' move')
                game_over = self.make_iteration(player)
                self.board.show()

                if game_over:
                    break

    # on each iteration player try's to make a move
    def make_iteration(self, player: Player):
        while True:
            y, x = input_('input coordinates row col:')
            status = 'REPEAT'
            try:
                status = self.move(player, int(y), int(x))
            except (IndexError, ValueError):
                print(f'Out of board size, current is {self.board.size}')

            if status == 'WIN':
                print(player.name + ' WIN!')
                return True
            elif status == 'REPEAT':
                continue
            return False

    # player make move by setting his player_id in board.field[y][x]
    def move(self, player: Player, y: int, x: int):
        if self.board.field[y][x] != 0:
            print('Cell in use')
            return 'REPEAT'

        self.board.cell_set(y, x, player.player_id)
        if player.has_won(y, x):
            return 'WIN'
        return 'OK'
