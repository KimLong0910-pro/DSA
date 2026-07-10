def insertion_s(a, k):
    n = len(a)

    for i in range(1, min(k + 1, n)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    return a


a = [4, 3, 2, 1]
k = 1
kqua = insertion_s(a, k)
print(a)
