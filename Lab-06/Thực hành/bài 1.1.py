myStack = []  # Khởi tạo một stack rỗng bằng list
myStack.append("data science")  # Thêm (Push) phần tử 'data science' vào đỉnh stack
myStack.append("data analytics")
myStack.append("data structures and algorithms")
myStack.append("big data")
myStack.append("learning data analytics")
myStack  # Hiển thị các phần tử hiện tại trong stack

myStack.pop()  # Lấy ra và xóa (Pop) phần tử ở đỉnh stack ('learning data analytics')
myStack.pop()  # Tiếp tục lấy ra và xóa phần tử ở đỉnh mới ('big data')
print(myStack)  # Hiển thị lại trạng thái stack sau khi pop
#