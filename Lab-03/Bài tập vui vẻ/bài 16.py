def so_nghich_the(a):
    n = len(a)
    dem = 0

    for i in range(n-1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                dem += 1

    return dem


a = [2, 3, 1]

kqua = so_nghich_the(a)
print(f"Số nghịch thế: {kqua}")
print(f"Số swap của Bubble Sort: {kqua}")