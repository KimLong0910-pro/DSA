import heapq


def dem_duong_shortest(do_thi, bdau):
    n = len(do_thi)
    vo_cuc = float("inf")

    khoang_cach = [vo_cuc] * n
    dem = [0] * n

    khoang_cach[bdau] = 0
    dem[bdau] = 1

    heap = [(0, bdau)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        if dist_u > khoang_cach[u]:
            continue

        for v, weight in do_thi[u]:
            new_dist = dist_u + weight

            if new_dist < khoang_cach[v]:
                khoang_cach[v] = new_dist
                dem[v] = dem[u]
                heapq.heappush(heap, (new_dist, v))

            elif new_dist == khoang_cach[v]:
                dem[v] += dem[u]

    return khoang_cach, dem


g1 = [[(1, 1), (2, 1)], [(3, 1)], [(3, 1)], []]

khoang_cach, dem = dem_duong_shortest(g1, 0)

print(f"Distances: {khoang_cach}")
print(f"Count: {dem}")
