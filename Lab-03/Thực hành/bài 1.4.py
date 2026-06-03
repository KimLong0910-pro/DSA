# Thực hành 01.4:
# thuật toán bubble sort – kết quả đầu ra là mảng sắp xếp từ lớn đến bé


def bubbleSortDescending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ví dụ thử nghiệm với một mảng số
arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
kqua = bubbleSortDescending(arr)
print(f"Mảng sau khi sắp xếp từ lớn đến bé: {kqua}")
