class Cell:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError

    def dec(self):
        if self.value != 0:
            self.value -= 1

    def inc(self):
        if self.value != 255:
            self.value += 1
        else:
            self.value = 0

class CellsList(list):
    def __init__(self):
        super(CellsList, self).__init__([Cell() for _ in range(256)])

    def __getitem__(self, index):
        if index == len(self):
            self.append(Cell()) # add a new cell

        return super(CellsList, self).__getitem__(index)