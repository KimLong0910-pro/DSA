from collections import deque


def round_robin(time, quantum):
    queue = deque()

    for i in range(len(time)):
        queue.append(i)

    thoi_diem = 0
    hoan_thanh = [0] * len(time)

    while queue:
        tien_trinh = queue.popleft()

        if time[tien_trinh] > quantum:
            time[tien_trinh] -= quantum
            thoi_diem += quantum
            queue.append(tien_trinh)
        else:
            thoi_diem += time[tien_trinh]
            hoan_thanh[tien_trinh] = thoi_diem
            time[tien_trinh] = 0

    return hoan_thanh


time = [5, 3, 1]
quantum = 2
kqua = round_robin(time, quantum)

print(f"Thời điểm hoàn thành: {kqua}")
