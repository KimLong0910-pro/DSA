myQueue = []  # Khởi tạo một hàng đợi (queue) rỗng bằng list
myQueue.append(
    "data science"
)  # Thêm (Enqueue) phần tử 'data science' vào cuối hàng đợi
myQueue.append("data analytics")
myQueue.append("data structures and algorithms")
myQueue.append("big data")
myQueue.append("learning data analytics")
print(myQueue)  # Hiển thị các phần tử hiện tại trong hàng đợi

print(
    myQueue.pop(0)
)  # Lấy ra và xóa (Dequeue) phần tử đầu tiên ở vị trí chỉ mục 0 ('data science')
print(
    myQueue.pop(0)
)  # Tiếp tục lấy ra và xóa phần tử đầu tiên kế tiếp ('data analytics')
print(myQueue)  # Hiển thị lại trạng thái hàng đợi sau khi thực hiện dequeue
