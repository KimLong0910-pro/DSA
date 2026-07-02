import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [
            [0 for column in range(dinh)] for row in range(dinh)
        ]

    def inketqua(cung, L, a):
        ten_dinh = ["a", "b", "c", "d", "e", "z"]
        dinh_nguon = ten_dinh[a]

        print(f"đỉnh nguồn xuất phát từ: {dinh_nguon}")
        for nut in range(cung.x):
            do_dai = (
                L[nut] if L[nut] != sys.maxsize else "Vô cùng (Không tới được)"
            )
            print(
                f"Đường đi ngắn nhất từ {dinh_nguon} đến {ten_dinh[nut]} có độ dài là: {do_dai}"
            )

    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        min_index = -1

        for x in range(cung.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x

        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x

        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            if u == -1:
                break
            P[u] = True

            for x in range(cung.x):
                if (
                    cung.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + cung.graph[u][x]
                ):
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


# Khởi tạo đồ thị có hướng gồm 6 đỉnh dựa trên Hình 1
g = Graph(6)
g.graph = [
    [0, 3, 0, 4, 0, 0],  # a (0)
    [0, 0, 6, 2, 0, 0],  # b (1)
    [0, 0, 0, 0, 4, 3],  # c (2)
    [0, 0, 1, 0, 4, 0],  # d (3)
    [0, 0, 0, 0, 0, 5],  # e (4)
    [0, 0, 0, 0, 0, 0],  # z (5)
]

# Tìm đường đi ngắn nhất bắt đầu từ đỉnh 'a' (chỉ mục số 0)
g.timduongdi(0)