class solution:
    def round_robin(self, processes, quantum):
        queue = processes[:]
        time = 0
        hoan_thanh = {}

        while queue:
            pid, burst = queue.pop(0)

            if burst <= quantum:
                time += burst
                hoan_thanh[pid] = time
            else:
                time += quantum
                queue.append((pid, burst - quantum))

        return hoan_thanh


s = solution()
processes = [("P1", 5), ("P2", 4), ("P3", 2)]

print(s.round_robin(processes, 2))
