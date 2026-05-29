def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
    else:
        return -1


array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x = 110
n = len(array)
kqua = tuyen_tinh(array, n, x)
print(f"phan tu tim thay duoc tai vi tri la: {kqua}")


def tuyen_tinh2(array2, n2, x2):
    for i in range(0, n2):
        if array2[i] == x2:
            return i
    else:
        return -1


array2 = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x2 = 185
n2 = len(array2)
kqua2 = tuyen_tinh2(array2, n2, x2)
print(f"phan tu khong duoc tim thay trong arr[]: {kqua2}")
