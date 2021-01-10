import numpy as np


class Board:
    def __init__(self, size: int):
        self.ZERO_ARRAY_: np.array = np.zeros((size, size), dtype=int)
        self.size: int = size
        self.field: np.array = self.ZERO_ARRAY_.copy()

    def cell_set(self, y: int, x: int, player_id: int):
        self.field[y][x] = player_id

    def player_field_get(self, player_id: int) -> np.array:
        return np.where(self.field == player_id, self.field, self.ZERO_ARRAY_.copy()).copy() // player_id

    def clear(self):
        self.field: np.array = self.ZERO_ARRAY_.copy()

    def show(self):
        print('--')
        for i in self.field:
            print(i)
