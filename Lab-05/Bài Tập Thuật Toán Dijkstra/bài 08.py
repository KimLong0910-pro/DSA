def dijkstra(do_thi, bdau):
    n = len(do_thi)
    vo_cuc = float("inf")

    khoang_cach = [vo_cuc] * n
    visited = [False] * n

    khoang_cach[bdau] = 0

    for _ in range(n):
        u = -1
        min_khoang_cach = vo_cuc

        for i in range(n):
            if not visited[i] and khoang_cach[i] < min_khoang_cach:
                min_khoang_cach = khoang_cach[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if do_thi[u][v] > 0 and not visited[v]:
                new_dist = khoang_cach[u] + do_thi[u][v]

                if new_dist < khoang_cach[v]:
                    khoang_cach[v] = new_dist

    return khoang_cach


def dem_dinh(do_thi, bdau, D):
    khoang_cach = dijkstra(do_thi, bdau)

    dem = 0

    for dist in khoang_cach:
        if dist <= D:
            dem += 1

    for i in range(len(khoang_cach)):
        if khoang_cach[i] <= D:
            print(i)

    return dem


g1 = [
    [0, 3, 1, 0, 0],
    [3, 0, 7, 5, 1],
    [1, 7, 0, 2, 0],
    [0, 5, 2, 0, 7],
    [0, 1, 0, 7, 0],
]

D = 3

kqua = dem_dinh(g1, 0, D)
print(f"Kết quả: {kqua}")
