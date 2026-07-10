def insertion(a):
    n = len(a)
    so_sanh = 0
    shift = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            so_sanh += 1

            if key < a[j]:
                a[j + 1] = a[j]
                shift += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return so_sanh, shift


def bubble(a):
    n = len(a)
    so_sanh = 0
    swap = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            so_sanh += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1

    return so_sanh, swap


def selection(a):
    n = len(a)
    so_sanh = 0
    swap = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            so_sanh += 1

            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return so_sanh, swap


a = [5, 1, 4, 2, 8]

print(f"Insertion: {insertion(a.copy())}")
print(f"Bubble: {bubble(a.copy())}")
print(f"Selection: {selection(a.copy())}")
