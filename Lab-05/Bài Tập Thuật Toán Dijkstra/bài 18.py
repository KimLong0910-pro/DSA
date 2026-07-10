def dijkstra(do_thi, s):
    n = len(do_thi)
    vo_cuc = float("inf")

    dist = [vo_cuc] * n
    visited = [False] * n

    dist[s] = 0

    for _ in range(n):
        u = -1
        min_dist = vo_cuc

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if do_thi[u][v] != 0 and not visited[v]:
                new_dist = dist[u] + do_thi[u][v]

                if new_dist < dist[v]:
                    dist[v] = new_dist

    return dist


do_thi = [[0, 2, 5], [0, 0, 0], [0, -4, 0]]

kqua = dijkstra(do_thi, 0)

print(kqua)
