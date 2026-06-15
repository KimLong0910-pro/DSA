# Dò từ phải sang trái
def chen_tu_phai(a):
    n = len(a)
    so_sanh = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            so_sanh += 1

            if key < a[j]:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return so_sanh


# Dò từ trái sang phải
def chen_tu_trai(a):
    n = len(a)
    so_sanh = 0

    for i in range(1, n):
        key = a[i]
        pos = i

        for j in range(i):
            so_sanh += 1

            if key < a[j]:
                pos = j
                break

        for j in range(i, pos, -1):
            a[j] = a[j - 1]

        a[pos] = key

    return so_sanh


a = [1, 2, 4, 3, 5]

phai = chen_tu_phai(a.copy())
trai = chen_tu_trai(a.copy())

print(f"Từ phải: {phai}")
print(f"Từ trái: {trai}")
