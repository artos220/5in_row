import numpy as np
from Board import Board
from Player import Player


class Game:
    def __init__(self, board: Board, players: [Player]):
        self.zero_array: np.array = np.zeros((board.size, board.size), dtype=int)
        self.board = board
        self.players = players

    def player_field_get(self, player_id):
        return np.where(self.board.field == player_id, self.board.field, self.zero_array) // player_id

    def move(self, player_id, x, y):
        if self.board.field[x][y] == 0:
            self.board.field[x][y] = player_id
            if self.has_5in_row(player_id):
                return 'WIN'

    def has_5in_row(self, player_id):
        target = 2
        player_field = self.player_field_get(player_id)
        x = (np.sum(player_field, axis=0))
        for i in x:
            if (np.sum(i)) >= target:
                return True

        y = (np.sum(player_field, axis=1))
        for i in y:
            if (np.sum(i)) >= target:
                return True

        for i in range(self.board.size):
            # diagonal sum
            if (np.sum(player_field.diagonal(offset=i, axis1=0, axis2=1))) >= target:
                return True
            if (np.sum(player_field.diagonal(offset=i+1, axis1=1, axis2=0))) >= target:
                return True
            # fliplr diagonal sum
            if (np.sum(np.fliplr(player_field).diagonal(offset=i, axis1=0, axis2=1))) >= target:
                return True
            if (np.sum(np.fliplr(player_field).diagonal(offset=i+1, axis1=1, axis2=0))) >= target:
                return True
