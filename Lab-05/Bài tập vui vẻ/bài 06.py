def duong_min(do_thi, s, t):
    n = len(do_thi)
    vo_cuc = float("inf")
    khoang_cach = [vo_cuc] * n
    visited = [False] * n
    khoang_cach[s] = 0

    for _ in range(n):
        u = -1
        khoang_cach_min = vo_cuc

        for i in range(n):
            if not visited[i] and khoang_cach[i] < khoang_cach_min:
                khoang_cach_min = khoang_cach[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        if u == t:
            return khoang_cach[t]

        for v in range(n):
            if do_thi[u][v] > 0 and not visited[v]:
                if khoang_cach[u] + do_thi[u][v] < khoang_cach[v]:
                    khoang_cach[v] = khoang_cach[u] + do_thi[u][v]

    if khoang_cach[t] == vo_cuc:
        return -1

    return khoang_cach[t]


g1 = [
    [0, 3, 1, 0, 0],
    [3, 0, 7, 5, 1],
    [1, 7, 0, 2, 0],
    [0, 5, 2, 0, 7],
    [0, 1, 0, 7, 0],
]

s = 0
t = 4
kqua = duong_min(g1, s, t)

print(kqua)
