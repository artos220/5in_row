import numpy as np
from Board import Board
from Player import Player


class Game:
    def __init__(self, board: Board, players: [Player]):
        self.zero_array: np.array = np.zeros((board.size, board.size), dtype=int)
        self.board: Board = board
        self.players: [Player] = players

    def move(self, player: Player, x: int, y: int):
        if self.board.field[x][y] == 0:
            self.board.player_id_cell_set(x, y, player.player_id)
            player.field_set(self.board.player_field_get(player.player_id))
            has5_in_row = player.has_5in_row()
            if has5_in_row:
                return 'WIN'

