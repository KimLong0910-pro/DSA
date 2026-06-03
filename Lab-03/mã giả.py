# n = số phần tử của mảng a
# lặp i từ 0 đến n-2:
#     daDoiCho = sai
#     lặp j từ 0 đến n-2-i:          # phần đuôi đã đúng chỗ nên không xét nữa
#         nếu a[j] > a[j+1]:
#             đổi chỗ a[j] và a[j+1]
#             daDoiCho = đúng
#     nếu daDoiCho == sai:
#         dừng                       # cả lượt không đổi gì → mảng đã sắp xếp


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        da_doi_cho = False
        for j in range(n - 1 - i):        # bỏ qua phần đuôi đã cố định
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi_cho = True
        if not da_doi_cho:                # dừng sớm khi đã sắp xếp xong
            break
    return a

