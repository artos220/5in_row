import numpy as np


class Board:
    def __init__(self, size: int):
        self.zero_array: np.array = np.zeros((size, size), dtype=int)
        self.size: int = size
        self.field: np.array = self.zero_array.copy()

    def player_id_cell_set(self, x: int, y: int, player_id: int):
        self.field[x][y] = player_id

    def player_field_get(self, player_id: int) -> np.array:
        return np.where(self.field == player_id, self.field, self.zero_array) // player_id

    def show(self):
        for i in self.field:
            print(i)
