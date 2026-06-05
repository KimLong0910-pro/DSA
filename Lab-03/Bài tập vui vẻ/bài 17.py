def bubble_k_luot(a, k):
    n = len(a)

    for i in range(min(k, n - 1)):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [3, 1, 4, 1, 5]
k = 2
kqua = bubble_k_luot(a, k)
print(kqua)