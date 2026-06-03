def cocktail_sort(a):
    left = 0
    right = len(a) - 1

    while left < right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

        right -= 1

        for i in range(right, left, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

        left += 1

    return a


a = [5, 1, 4, 2, 8]
kqua = cocktail_sort(a)
print(kqua)
