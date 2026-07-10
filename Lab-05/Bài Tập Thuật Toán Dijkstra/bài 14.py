import heapq


def duong_ngan_nhi(do_thi, s, t):
    n = len(do_thi)
    vo_cuc = float("inf")

    first_dist = [vo_cuc] * n
    second_dist = [vo_cuc] * n

    first_dist[s] = 0
    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        for v, weight in do_thi[u]:
            new_dist = dist_u + weight

            if new_dist < first_dist[v]:
                second_dist[v] = first_dist[v]
                first_dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

            elif first_dist[v] < new_dist < second_dist[v]:
                second_dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    if second_dist[t] == vo_cuc:
        return -1

    return second_dist[t]


g1 = [[(1, 1), (2, 2)], [(3, 3)], [(3, 4)], []]

kqua = duong_ngan_nhi(g1, 0, 3)
print(kqua)
