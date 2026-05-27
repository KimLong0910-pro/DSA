def tim_kiem_linh_canh(a, x):
    n = len(a)
    cuoi = a[n - 1]  
    a[n - 1] = x
    i = 0

    while a[i] != x:
        i += 1
    a[n - 1] = cuoi

    if i < n - 1 or cuoi == x:
        return i
    else: 
        return -1


a = [10, 22, 28, 29, 40]
x = 29

vi_tri = tim_kiem_linh_canh(a, x)
print(f"Vị trí: {vi_tri}")