def hash_key(key, m):  # Định nghĩa hàm băm (nhận khóa key và kích thước m)
    return key % m  # Trả về giá trị băm bằng phép toán chia lấy dư (Modulo)


m = 7
print(f"The hash value is {hash_key(15, m)}")  # In ra kết quả: The hash value is 1
print(f"The hash value is {hash_key(2, m)}")  # In ra kết quả: The hash value is 2
print(f"The hash value is {hash_key(3, m)}")  # In ra kết quả: The hash value is 3
print(f"The hash value is {hash_key(9, m)}")  # In ra kết quả: The hash value is 2
print(f"The hash value is {hash_key(11, m)}")  # In ra kết quả: The hash value is 4
print(f"The hash value is {hash_key(7, m)}")  # In ra kết quả: The hash value is 0
