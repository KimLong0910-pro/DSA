def tim_kiem_ma_tran(M, x):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == x:
                return i, j
    else:
        return -1, -1


M = [
    [5, 8, 1], 
    [3, 9, 7],
    [2, 6, 4]
]
x = 9

kqua = tim_kiem_ma_tran(M, x)
print(kqua)
