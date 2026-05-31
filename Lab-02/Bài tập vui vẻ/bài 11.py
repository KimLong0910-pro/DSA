def gia_tri_nho_nhat(a):
    left = 0
    right = len(a) - 1
    mid = 0

    while left < right:
        mid = (left + right) // 2

        if a[mid] > a[right]: 
            left = mid+1
        else: 
            right = mid

    return a[left]
    

a = [3,4,5,1,2]
gia_tri = gia_tri_nho_nhat(a)
print(f'Giá trị nhỏ nhất: {gia_tri}')

