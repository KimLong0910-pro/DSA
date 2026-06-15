def selection_swap(a):
    swap = 0
    n = len(a)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return swap


def bubble_swap(a):
    swap = 0
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1

    return swap


a = [3, 2, 1]

print(f"Selection: {selection_swap(a.copy())}")
print(f"Bubble: {bubble_swap(a.copy())}")