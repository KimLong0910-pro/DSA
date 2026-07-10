import heapq


def trong_so_dinh(do_thi, trong_so, s):
    n = len(do_thi)
    vo_cuc = float("inf")
    khoang_cach = [vo_cuc] * n
    khoang_cach[s] = trong_so[s]

    heap = [(khoang_cach[s], s)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        if dist_u > khoang_cach[u]:
            continue

        for v, weight in do_thi[u]:
            new_dist = dist_u + weight + trong_so[v]

            if new_dist < khoang_cach[v]:
                khoang_cach[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return khoang_cach


g1 = [[(1, 3), (2, 1)], [(3, 2)], [(3, 4)], []]

trong_so = [1, 2, 3, 4]
kqua = trong_so_dinh(g1, trong_so, 0)

print(kqua)
