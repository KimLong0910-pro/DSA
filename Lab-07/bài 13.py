def mergeIntervals(khoang_giao_nhau):
    if not khoang_giao_nhau:
        return []

    khoang_giao_nhau.sort(key=lambda x: x[0])
    kqua = [khoang_giao_nhau[0]]

    for current in khoang_giao_nhau[1:]:
        last = kqua[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            kqua.append(current)

    return kqua

khoang_giao_nhau = [[1, 3], [2, 6], [8, 10]]
print(mergeIntervals(khoang_giao_nhau))