def ktra_so_nguyen_to(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True


def so_nguyen_dau_tien(a):
    for vi_tri in range(len(a)):
        if ktra_so_nguyen_to(a[vi_tri]):
            return a[vi_tri], vi_tri
    else:
        return None, -1


a = [4, 6, 9, 7, 11]

gia_tri, vi_tri = so_nguyen_dau_tien(a)
print(f"Số nguyên tố đầu tiên: {gia_tri} - Vị trí: {vi_tri}")
