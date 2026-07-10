import heapq


def nhieu_nguon(do_thi, nguon):
    n = len(do_thi)
    vo_cuc = float("inf")

    khoang_cach = [vo_cuc] * n
    heap = []

    for s in nguon:
        khoang_cach[s] = 0
        heapq.heappush(heap, (0, s))

    while heap:
        dist_u, u = heapq.heappop(heap)

        if dist_u > khoang_cach[u]:
            continue

        for v, weight in do_thi[u]:
            new_dist = dist_u + weight

            if new_dist < khoang_cach[v]:
                khoang_cach[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return khoang_cach


g1 = [
    [(1, 3), (2, 1)],
    [(0, 3), (2, 7), (3, 5), (4, 1)],
    [(0, 1), (1, 7), (3, 2)],
    [(1, 5), (2, 2), (4, 7)],
    [(1, 1), (3, 7)],
]

kqua = nhieu_nguon(g1, [0, 3])
print(kqua)
