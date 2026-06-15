def online_insertion(stream):
    a = []

    for x in stream:
        a.append(x)

        key = a[-1]
        j = len(a) - 2

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

        print(a)


stream = [5, 2, 8, 1]

online_insertion(stream)