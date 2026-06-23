def dijkstra_path(do_thi, s, t):
    n = len(do_thi)
    vo_cuc = float("inf")

    dist = [vo_cuc] * n
    visited = [False] * n
    parent = [-1] * n

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
            if do_thi[u][v] > 0 and not visited[v]:
                new_dist = dist[u] + do_thi[u][v]

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u

    if dist[t] == vo_cuc:
        return -1, []

    path = []
    cur = t

    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    return dist[t], path


g1 = [
    [0, 4, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 2, 0, 5, 8, 0],
    [0, 0, 0, 0, 3, 6],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0]
]

dist, path = dijkstra_path(g1, 0, 4)

print(f"Shortest distance: {dist}")
print(f"Path: {path}")