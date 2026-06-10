def insertion_s(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    
    return a


a = ['d','a','c','b']
insertion_s(a)
print(a)