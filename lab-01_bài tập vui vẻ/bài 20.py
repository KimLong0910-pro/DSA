def them_lien_he(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    danh_ba.append({"tên": ten, "sdt": sdt})


def tim_sdt_theo_ten(danh_ba):
    ten = input("Nhập tên cần tìm: ")
    for i in danh_ba:
        if i["ten"] == ten:
            print(f"Số điện thoại: {i['sdt']}")
            return
    print("Không tìm thấy!")


def tim_ten_theo_sdt(danh_ba):
    sdt = input("Nhập số điện thoại cần tìm: ")
    for i in danh_ba:
        if i["sdt"] == sdt:
            print(f"Tên: {i['ten']}")
            return
    print("Không tìm thấy số điện thoại!")


def dem_dau_so(danh_ba):
    dau_so = input("Nhập 3 số đầu của số điện thoại: ")
    dem = 0
    for i in danh_ba:
        if i["sdt"].startswith(dau_so):
            dem += 1
    print(f"Số điện thoại có 3 số đầu {dau_so} là: {dem}")


def menu():
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm theo đầu số")
    print("5. Thoát")


def main():
    danh_ba = []

    while True:
        menu()
        chon = input("Chọn chức năng: ")

        if chon == "1":
            them_lien_he(danh_ba)
        elif chon == "2":
            tim_sdt_theo_ten(danh_ba)
        elif chon == "3":
            tim_ten_theo_sdt(danh_ba)
        elif chon == "4":
            dem_dau_so(danh_ba)
        elif chon == "5":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn này không có!")


main()
