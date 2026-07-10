vo_cuc = float("inf")


def dijkstra(do_thi, bdau):
    n = len(do_thi)
    khoang_cach = [vo_cuc] * n
    visited = [False] * n
    khoang_cach[bdau] = 0

    for _ in range(n):
        min_khoang_cach = vo_cuc
        u = -1

        for i in range(n):
            if not visited[i] and khoang_cach[i] < min_khoang_cach:
                min_khoang_cach = khoang_cach[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if do_thi[u][v] != 0 and not visited[v]:
                if khoang_cach[u] + do_thi[u][v] < khoang_cach[v]:
                    khoang_cach[v] = khoang_cach[u] + do_thi[u][v]

    return khoang_cach


g1 = [
    [0, 5, 3, 0, 0],
    [5, 0, 1, 2, 0],
    [3, 1, 0, 6, 0],
    [0, 2, 6, 0, 4],
    [0, 0, 0, 4, 0],
]

ten_dinh = ["A", "B", "C", "D", "E"]
kqua = dijkstra(g1, 0)

for i in range(len(kqua)):
    if kqua[i] == vo_cuc:
        print(f"{ten_dinh[i]}: -1")
    else:
        print(f"{ten_dinh[i]}: {kqua[i]}")
