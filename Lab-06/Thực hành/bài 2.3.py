from queue import Queue  # Nhập lớp Queue từ thư viện tích hợp sẵn của Python

q = Queue(
    maxsize=5
)  # Khởi tạo một hàng đợi chuyên dụng với kích thước tối đa là 5 phần tử
print(q.qsize())  # Hiển thị số lượng phần tử hiện tại trong hàng đợi (lúc này là 0)

q.put(
    "data analytics"
)  # Thêm (Enqueue) phần tử 'data analytics' vào cuối hàng đợi bằng phương thức put()
q.put("data structures and algorithms")
q.put("big data")
q.put("learning data analytics")
print(q.qsize())  # Hiển thị lại số lượng phần tử hiện tại (lúc này là 4)

print(
    q.get()
)  # Lấy ra và xóa (Dequeue) phần tử ở đầu hàng đợi bằng phương thức get() ('data analytics')
print(
    q.get()
)  # Tiếp tục lấy ra và xóa phần tử tiếp theo ở đầu hàng đợi ('data structures and algorithms')
