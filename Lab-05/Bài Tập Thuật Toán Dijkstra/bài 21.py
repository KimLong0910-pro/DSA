import heapq


def dijkstra_state(do_thi, s, t, fuel_limit):
    heap = [(0, s, fuel_limit)]
    visited = set()

    while heap:
        cost, u, fuel = heapq.heappop(heap)

        if (u, fuel) in visited:
            continue
        visited.add((u, fuel))

        if u == t:
            return cost

        for v, weight in do_thi[u]:
            if fuel > 0:
                heapq.heappush(heap, (cost + weight, v, fuel - 1))

    return -1


g1 = [[(1, 2), (2, 1)], [(3, 3)], [(3, 4)], []]

s = 0
t = 3
fuel_limit = 2
kqua = dijkstra_state(g1, s, t, fuel_limit)

print(kqua)
