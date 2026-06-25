from collections import (
    deque,
)  # Nhập lớp deque từ thư viện collections để tối ưu hiệu năng hàng đợi

q = deque()  # Khởi tạo một đối tượng hàng đợi rỗng bằng deque
q.append("data analytics")  # Thêm (Enqueue) phần tử 'data analytics' vào cuối hàng đợi
q.append("data structures and algorithms")
q.append("big data")
q.append("learning data analytics")
print(q)  # Hiển thị các phần tử hiện tại trong hàng đợi

print(
    q.popleft()
)  # Lấy ra và xóa (Dequeue) phần tử ở đầu hàng đợi một cách tối ưu ('data analytics')
print(
    q.popleft()
)  # Tiếp tục lấy ra và xóa phần tử tiếp theo ở đầu hàng đợi ('data structures and algorithms')
print(q)  # Hiển thị lại trạng thái hàng đợi sau khi dùng popleft
