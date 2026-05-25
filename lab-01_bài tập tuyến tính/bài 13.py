def ten_sv(ds, x):
    x = x.upper()
    for i in range(len(ds)):
        if ds[i].upper() == x:
            return i
    else:
        return -1


ds = ["An", "Bình", "Châu", "long", "LINH"]
x = input("Nhập tên: ")

kqua = ten_sv(ds, x)
print(f"Vị trí: {kqua}")
