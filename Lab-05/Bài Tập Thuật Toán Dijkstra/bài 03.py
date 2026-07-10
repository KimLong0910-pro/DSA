def dijkstra(do_thi, bdau):
    n = len(do_thi)
    khoang_cach = [float("inf")] * n
    visited = [False] * n
    khoang_cach[bdau] = 0

    for _ in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or khoang_cach[i] < khoang_cach[u]):
                u = i

        if khoang_cach[u] == float("inf"):
            break

        visited[u] = True

        for v, w in do_thi[u]:
            if not visited[v] and khoang_cach[u] + w < khoang_cach[v]:
                khoang_cach[v] = khoang_cach[u] + w

    return khoang_cach


g1 = [
    [(1, 3), (2, 1)],
    [(0, 3), (2, 2), (3, 4)],
    [(0, 1), (1, 2), (3, 3)],
    [(1, 4), (2, 3), (4, 3)],
    [(3, 3), (5, 2)],
    [(4, 2)],
]

khoang_cach = dijkstra(g1, 0)
print(khoang_cach)
