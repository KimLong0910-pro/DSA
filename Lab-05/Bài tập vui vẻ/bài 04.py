def dijkstra(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if u == -1 or dist[u] == float("inf"):
            break

        visited[u] = True

        for v, w in graph[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


graph = [
    [(1, 3), (2, 1)],
    [(0, 3), (2, 2), (3, 4)],
    [(0, 1), (1, 2), (3, 3)],
    [(1, 4), (2, 3), (4, 3)],
    [(3, 3), (5, 2)],
    [(4, 2)],
]

dist = dijkstra(graph, 0)
for i in range(len(dist)):
    if dist[i] == float("inf"):
        print(f"dist[{i}] = -1")
    else:
        print(f"dist[{i}] = {dist[i]}")
