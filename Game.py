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
        self.current_player: Player = players[0]
        self.game_over: bool = False

    def switch_player(self):
        curr_player_id = self.current_player.player_id
        if curr_player_id < len(self.players):
            self.current_player = self.players[curr_player_id]
        else:
            self.current_player = self.players[0]
        return curr_player_id

    def restart(self):
        self.board.clear()
        self.current_player = self.players[0]
        self.game_over = False
        for player in self.players:
            player.clear()

    def start(self):
        self.board.show()
        while not self.game_over:
            for player in self.players:
                print(player.name + ' move')
                self.game_over = self.make_iteration(player)
                self.board.show()

                if self.game_over:
                    break

    # on each iteration player try's to make a move
    def make_iteration(self, player: Player, x: int, y: int):
        while True:
            # y, x = input_('input coordinates row col:')
            status = 'REPEAT'
            try:
                status = self.move(player, int(y), int(x))
            except (IndexError, ValueError):
                print(f'Out of board size, current is {self.board.size}')

            if status == 'WIN':
                print(player.name + ' WIN!')
                self.game_over = True
                return True
            elif status == 'REPEAT':
                continue
            elif status == 'PASS':
                pass
            elif status == 'BREAK':
                break

            self.switch_player()
            return False

    # player make move by setting his player_id in board.field[y][x]
    def move(self, player: Player, y: int, x: int):
        if self.board.field[y][x] != 0:
            print('Cell in use')
            # return 'REPEAT'
            return 'BREAK'

        self.board.cell_set(y, x, player.player_id)
        if player.has_won(y, x):
            return 'WIN'
        return 'OK'
