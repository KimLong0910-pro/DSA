def display_hash(hashTable):  # Định nghĩa hàm hiển thị cấu trúc bảng băm hiện tại
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [
    [] for _ in range(10)
]  # Khởi tạo bảng băm gồm 10 danh sách rỗng (kích thước m = 10)


def Hashing(keyvalue):  # Hàm băm dùng phương pháp chia lấy dư: keyvalue % 10
    return keyvalue % len(HashTable)


def insert(
    Hashtable, keyvalue, value
):  # Hàm thêm một phần tử (value) vào bảng băm dựa trên khóa (keyvalue)

    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


# Thực hiện chèn các cặp (Khóa, Giá trị) vào bảng băm HashTable:
insert(HashTable, 10, "MachineLearning")  # 10 % 10 = 0 -> Chèn vào chỉ mục 0
insert(HashTable, 45, "DataScience")  # 45 % 10 = 5 -> Chèn vào chỉ mục 5
insert(
    HashTable, 20, "DataAnalytics"
)  # 20 % 10 = 0 -> Chèn vào chỉ mục 0 (Xảy ra va chạm)
insert(HashTable, 9, "BigData")  # 9 % 10 = 9  -> Chèn vào chỉ mục 9
insert(HashTable, 21, "DataStructure ")  # 21 % 10 = 1 -> Chèn vào chỉ mục 1
insert(HashTable, 41, "IoT")  # 41 % 10 = 1 -> Chèn vào chỉ mục 1 (Xảy ra va chạm)
insert(
    HashTable, 35, "Probability"
)  # 35 % 10 = 5 -> Chèn vào chỉ mục 5 (Xảy ra va chạm)

display_hash(HashTable)  # Gọi hàm hiển thị toàn bộ kết quả bảng băm ra màn hình
