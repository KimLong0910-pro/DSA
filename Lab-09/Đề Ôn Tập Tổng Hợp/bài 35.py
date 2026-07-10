def mergeIntervals(giao_nhau):
    if not giao_nhau:
        return []

    giao_nhau.sort(key=lambda x: x[0])
    kqua = [giao_nhau[0]]

    for current in giao_nhau[1:]:
        last = kqua[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            kqua.append(current)

    return kqua


giao_nhau = [[1, 3], [2, 6], [8, 10]]
print(mergeIntervals(giao_nhau))
