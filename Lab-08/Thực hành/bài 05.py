import sys


class Graph:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print("đỉnh nguồn xuất phát từ: ")
        for nut in range(cung.x):
            print(a, "đến đỉnh", nut, "độ dài đường đi là: ", L[nut])

    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        min_index = -1  # Khởi tạo giá trị mặc định tránh lỗi logic nếu không tìm thấy

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
            P[u] = True

            for x in range(cung.x):
                # Sửa lỗi logic nối dòng (+) trong ảnh đưa về đúng một dòng hoàn chỉnh
                if (
                    cung.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + cung.graph[u][x]
                ):
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


# Khởi tạo đồ thị có hướng gồm 6 đỉnh (0 đến 5)
g = Graph(6)
g.graph = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 6, 2, 0, 0],
    [0, 0, 0, 0, 4, 3],
    [0, 0, 1, 0, 4, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]

# Chạy thuật toán tìm đường đi ngắn nhất từ đỉnh nguồn số 0
g.timduongdi(0)
