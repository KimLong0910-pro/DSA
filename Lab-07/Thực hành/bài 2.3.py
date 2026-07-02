from collections import deque

deque()
deque([{"data": "a"}, {"data": "b"}])

llist = deque("abcd")  # Khởi tạo một deque chứa các ký tự: deque(['a', 'b', 'c', 'd'])
llist  # Màn hình sẽ hiển thị kết quả của llist hiện tại: deque(['a', 'b', 'c', 'd'])

llist.append("h")  # Thêm ký tự 'h' vào phía bên phải (cuối) của deque
llist  # Màn hình hiển thị llist mới: deque(['a', 'b', 'c', 'd', 'h'])

llist.pop()  # Lấy ra và xóa phần tử cuối cùng bên phải (là 'h'). Màn hình sẽ in ra: 'h'
llist  # Màn hình hiển thị llist sau khi pop: deque(['a', 'b', 'c', 'd'])


d = deque([1, 2, 3, 4, 5, 6])
print(d)  # Màn hình in ra: deque([1, 2, 3, 4, 5, 6])

for i in d:
    print(i)  # Vòng lặp in ra từng số từ 1 đến 6 trên từng dòng riêng biệt

print(d.pop(), d)  # Hàm d.pop() lấy số 6 ra, phần còn lại của d là [1, 2, 3, 4, 5].
#          -> Màn hình sẽ in ra kết quả của cặp (giá trị bị pop, deque còn lại):
#             6 deque([1, 2, 3, 4, 5])
