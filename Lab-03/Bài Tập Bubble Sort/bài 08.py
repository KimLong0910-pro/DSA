def bubble_sort(a, k):
    n = len(a)

    for i in range(min(k, n - 1)):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False
    return True


a = [3, 2, 1]
k = 1
kqua = bubble_sort(a, k)
print(kqua)
