class DynamicMatrix:
    def __init__(self, hang, cot):
        self.data = [[0 for _ in range(cot)] for _ in range(hang)]

    def addRow(self):
        cot = len(self.data[0])
        self.data.append([0] * cot)

    def addCol(self):
        for row in self.data:
            row.append(0)

    def set(self, i, j, val):
        self.data[i][j] = val

    def get(self, i, j):
        return self.data[i][j]


ma_tran = DynamicMatrix(2, 2)

ma_tran.set(0, 1, 7)
ma_tran.addRow()
ma_tran.addCol()

print(ma_tran.get(0, 1))
print(ma_tran.data)
