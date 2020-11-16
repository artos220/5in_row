import numpy as np


class Player:
    def __init__(self, name: str, player_id: int):
        # self.zero_array: np.array = np.zeros((board.size, board.size), dtype=int)
        self.name = name
        self.player_id = player_id
        # self.field: np.array = self.zero_array.copy()
