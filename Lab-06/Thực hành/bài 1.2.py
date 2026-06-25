from collections import (
    deque,
)  # Nhập lớp deque từ thư viện collections để tối ưu hóa hiệu năng stack

myStack = deque()  # Khởi tạo một đối tượng stack rỗng bằng deque
myStack.append("data science")  # Thêm (Push) phần tử 'data science' vào đỉnh stack
myStack.append("data structures and algorithms")
myStack.append("learning data analytics")
myStack.append("big data")
myStack  # Hiển thị các phần tử hiện tại trong stack

myStack.pop()  # Lấy ra và xóa (Pop) phần tử ở đỉnh stack ('big data')
myStack.pop()  # Tiếp tục lấy ra và xóa phần tử ở đỉnh mới ('learning data analytics')
print(myStack)  # Hiển thị lại trạng thái stack sau khi pop
