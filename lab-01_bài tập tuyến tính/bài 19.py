def tim_sinh_vien(ds, mssv):
    for sv in ds:
        if sv["mssv"] == mssv:
            print("Tìm thấy sinh viên:")
            print(f"MSSV: {sv['mssv']}")
            print(f"Họ tên: {sv['ho_ten']}")
            print(f"Điểm TB: {sv['dtb']}")
            return
    print(f"Không tìm thấy sinh viên có mã: {mssv}")


ds = [
    {"mssv": "sv1", "ho_ten": "An", "dtb": 8.5},
    {"mssv": "sv2", "ho_ten": "Bình", "dtb": 7.2},
    {"mssv": "sv3", "ho_ten": "Chi", "dtb": 9.0},
]

tim_sinh_vien(ds, "sv2")
tim_sinh_vien(ds, "sv5")
