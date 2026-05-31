def tim_gia_tri(ma_tran, x):
    m = len(ma_tran)
    n = len(ma_tran[0])
    left = 0
    right = m * n - 1

    while left < right:
        mid = (left + right) // 2

        i = mid // n
        j = mid % n
        gia_tri = ma_tran[i][j]

        if gia_tri == x:
            return True

        if gia_tri < x:
            left = mid + 1
        else:
            right = mid - 1

    return False


ma_tran = [
    [1, 3, 5],
    [7, 9, 11]
]

x = 9

kqua = tim_gia_tri(ma_tran, x)
print(f"Giá trị {x}: {kqua}")
