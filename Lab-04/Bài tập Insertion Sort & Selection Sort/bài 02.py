def insertion_s(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


a = [23, 7, 21, 28, 19, 12, 9, 22, 27]
insertion_s(a)
print(a)