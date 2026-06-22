import heapq


def dijkstra_heap(do_thi, bdau):
    n = len(do_thi)
    vo_cuc = float("inf")

    khoang_cach = [vo_cuc] * n
    khoang_cach[bdau] = 0

    heap = [(0, bdau)]

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
    [(1, 1), (3, 7)]
]

kqua = dijkstra_heap(g1, 0)
print(kqua)