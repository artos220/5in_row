import numpy as np


class Board:
    def __init__(self, size: int):
        self.zero_array: np.array = np.zeros((size, size), dtype=int)
        self.size = size
        self.field: np.array = self.zero_array.copy()

    def show(self):
        for i in self.field:
            print(i)
