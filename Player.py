import numpy as np
import itertools


def has5in_row(row):
    """
    :param row: current matrix line, need 5 in row
    """
    # TODO declare groups as array
    groups = []
    for k, g in itertools.groupby(row):
        groups.append(sum(list(g)))
    if (np.array(groups).max()) >= 5:
        return True


class Player:
    def __init__(self, name: str, player_id: int, size: int):
        self.name: str = name
        self.player_id: int = player_id
        self.field: np.array = np.zeros((size, size), dtype=int)  # player field
        self.size = size  # filed size

    def has_won(self, y: int, x: int):
        """
        update the player's field and check his score
        :param x: column
        :param y: row
        """
        self.field[y][x] = 1

        # check player score for x,y coordinates in row, column, diagonal, anti-diagonal
        if has5in_row(self.field[y].copy()) \
                or has5in_row(np.transpose(self.field[:, x].copy())) \
                or has5in_row(self.field.diagonal(offset=x-y).copy()) \
                or has5in_row(np.fliplr(self.field).diagonal(offset=self.size-1-x-y).copy()):
            return True
