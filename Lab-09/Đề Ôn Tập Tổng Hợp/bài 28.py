from collections import deque


def bfs(do_thi, bdau):
    visited = [False] * len(do_thi)
    queue = deque([bdau])
    visited[bdau] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for ke in do_thi[node]:
            if not visited[ke]:
                visited[ke] = True
                queue.append(ke)


do_thi = [[1, 2], [3], [4], [], []]
bfs(do_thi, 0)

