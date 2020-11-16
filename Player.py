import numpy as np


def update_row(row, x):
    """
    проходит по строке и увеличивает значение соседних ячеек для x на 1, если в них уже есть 1
    :param row: строка с элементами
    :param x: номер элемента
    """
    # соседи слева
    while x >= 0:
        if row[x] > 0:
            row[x] += 1
            x -= 1
        break
    # соседи справа
    while x < len(row):
        if row[x+1] > 0:
            row[x+1] += 1
            x += 1
        break
    return row


class Player:
    def __init__(self, name: str, player_id: int):
        self.name: str = name
        self.player_id: int = player_id
        # все ходы игрока
        self.field: np.array = None

        # матрицы со счетом игрока, если в строке будет 5, то победа
        self.field_rows: np.array = None
        self.field_columns: np.array = None
        self.field_left: np.array = None
        self.field_right: np.array = None

    def field_update(self, x: int, y: int):
        """
        обновление счета игрока
        увеличивает соседние ячейки для x,y на 1, если в них уже есть 1
        и так для строк/колонок/дигоналей
        :param x: columns
        :param y: rows
        """
        self.field[x][y] = 1
        size = len(self.field)

        # rows
        self.field_rows[x][y] = 1
        self.field_rows[y] = update_row(self.field_rows[y], x)

        # columns
        self.field_columns[x][y] = 1
        self.field_columns[x] = update_row(np.fliplr(self.field_columns[x]), y)

        # ldiagonal
        # rdiagonal

    def has_5in_row(self):
        target = 2

        x = (np.sum(self.field, axis=0))
        for i in x:
            if (np.sum(i)) >= target:
                return True

        y = (np.sum(self.field, axis=1))
        for i in y:
            if (np.sum(i)) >= target:
                return True

        for i in range(self.field.size):
            # diagonal sum
            if (np.sum(self.field.diagonal(offset=i, axis1=0, axis2=1))) >= target:
                return True
            if (np.sum(self.field.diagonal(offset=i + 1, axis1=1, axis2=0))) >= target:
                return True
            # fliplr diagonal sum
            if (np.sum(np.fliplr(self.field).diagonal(offset=i, axis1=0, axis2=1))) >= target:
                return True
            if (np.sum(np.fliplr(self.field).diagonal(offset=i + 1, axis1=1, axis2=0))) >= target:
                return True