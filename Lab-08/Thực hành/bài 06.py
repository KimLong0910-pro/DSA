import sys


class Graph:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        # Danh sách ánh xạ số chỉ mục thành ký tự chữ cái tương ứng
        ten_dinh = ["a", "b", "c", "f", "g", "z"]
        dinh_nguon = ten_dinh[a]

        print(f"đỉnh nguồn xuất phát từ: {dinh_nguon}")
        for nut in range(cung.x):
            do_dai = L[nut] if L[nut] != sys.maxsize else "Vô cùng (Không tới được)"
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
            if u == -1:  # Nếu không còn đỉnh nào đến được thì dừng vòng lặp sớm
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


# Khởi tạo đồ thị có hướng gồm 6 đỉnh
g = Graph(6)
g.graph = [
    [0, 3, 0, 1, 0, 0],  # a (0)
    [0, 0, 7, 0, 0, 0],  # b (1)
    [0, 0, 0, 0, 0, 3],  # c (2)
    [0, 0, 9, 0, 2, 0],  # f (3)
    [0, 0, 3, 0, 0, 7],  # g (4)
    [0, 0, 0, 0, 0, 0],  # z (5)
]

# Chạy thuật toán tìm đường đi ngắn nhất từ đỉnh nguồn 'a' (chỉ mục số 0)
g.timduongdi(0)
