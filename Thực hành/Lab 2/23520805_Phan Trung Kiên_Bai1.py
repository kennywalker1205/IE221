#23520805_Phan Trung Kiên
class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.so_sp = so_sp
        self.luong_ht = 0

    def in_nv(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.so_sp, self.luong_ht])

    @staticmethod
    def init_nv():
        """1.Khởi tạo dữ liệu nhân viên"""
        ds = []
        nv1 = NhanVien(101, "Nguyễn Văn A", 4_500_000, 42)
        nv2 = NhanVien(102, "Trần Thị B", 5_000_000, 15)
        nv3 = NhanVien(103, "Lê Hoàng C", 6_000_000, 28)
        nv4 = NhanVien(104, "Phạm Minh D", 4_000_000, 55)
        nv5 = NhanVien(105, "Vũ Đức E", 7_500_000, 10)
        nv6 = NhanVien(106, "Hoàng Bích F", 5_500_000, 33)
        nv7 = NhanVien(107, "Phan Trọng G", 4_800_000, 48)
        nv8 = NhanVien(108, "Đỗ Việt H", 8_000_000, 5)
        nv9 = NhanVien(109, "Ngô Thanh I", 3_500_000, 60)
        nv10 = NhanVien(110, "Bùi Xuân J", 4_200_000, 22)
        nv11 = NhanVien(111, "Lý Hải K", 6_500_000, 18)
        nv12 = NhanVien(112, "Dương Gia L", 5_200_000, 39)
        nv13 = NhanVien(113, "Trịnh Công M", 4_900_000, 41)
        nv14 = NhanVien(114, "Đặng Thu N", 5_800_000, 25)
        nv15 = NhanVien(115, "Mai Thế O", 7_000_000, 12)
        nv16 = NhanVien(116, "Trần Hữu P", 4_600_000, 50)
        nv17 = NhanVien(117, "Nguyễn Kha Q", 5_100_000, 29)
        nv18 = NhanVien(118, "Bùi Lan R", 6_200_000, 20)
        nv19 = NhanVien(119, "Vũ Văn S", 4_300_000, 45)
        nv20 = NhanVien(120, "Phạm Quỳnh T", 5_900_000, 31)

        ds.extend([
            nv1, nv2, nv3, nv4, nv5, nv6, nv7, nv8, nv9, nv10,
            nv11, nv12, nv13, nv14, nv15, nv16, nv17, nv18, nv19, nv20
        ])

        return ds

    def print_nv(ds):
        """2. In các nhân viên trong công ty"""
        for nv in ds:
            nv.in_nv()

    def tinh_luong_ht(self):
        """3. Tính lương các nhân viên"""
        luong = self.luong_cb + self.so_sp * 175_000
        if luong >= 10_000_000: luong += luong * 0.1

        self.luong_ht += int(luong)
        return luong

    def tim_nv_theo_ma_nv(ds, ma_nv):
        """4. Tìm nhân viên theo mã nhân viên"""
        return next(filter(lambda nv: nv.ma_nv == ma_nv, ds), None)

    def cap_nhat_luong_cb_theo_ma_nv(ds, ma_nv, luong_new):
        """5. Cập nhật lương cơ bản theo mã nhân viên"""
        nv = NhanVien.tim_nv_theo_ma_nv(ds, ma_nv)
        if nv:
            nv.luong_cb = luong_new
            nv.tinh_luong_ht()
            return nv
        else:
            return None

    def tim_nv_co_luong_cao_nhat(ds):
        """6. Tìm nhân viên có lương cao nhất"""
        nv_max = max(ds, key = lambda nv: nv.luong_ht)
        return nv_max

    def tim_nv_co_so_sp_thap_nhat(ds):
        """7. Tìm nhân viên có số sản phẩm bán được thấp nhất"""
        nv_sp_min = min(ds, key = lambda nv: nv.so_sp)
        return nv_sp_min

    def tim_10_nv_co_luong_cao_nhat(ds):
        """8. Tìm 10 nhân viên có lương cao nhất"""
        ds_sorted = sorted(ds, key = lambda nv: nv.luong_ht, reverse = True)
        return ds_sorted[:10]

    def sap_xep_nv_luong_ht_tang_dan(ds):
        """9. Sắp xếp nhân viên tăng dần theo lương hàng tháng"""
        ds_sorted = sorted(ds, key = lambda nv: nv.luong_ht)
        return ds_sorted

    def xoa_nv_theo_ma_nv(ds, ma_nv):
        """10. Tự xây dựng thêm thao tác thích hợp cho bài toán (Xóa nhân viên theo mã nhân viên)"""
        nv_can_xoa = NhanVien.tim_nv_theo_ma_nv(ds, ma_nv)
        if nv_can_xoa:
            ds.remove(nv_can_xoa)
            print(f"\t Xóa nhân viên có mã {ma_nv}")
            return True
        else:
            print(f"\t Không tìm thấy nhân viên có mã {ma_nv}")
            return False

    def tinh_tong_quy_luong_phai_tra(ds):
        """10. 10. Tự xây dựng thêm thao tác thích hợp cho bài toán (Tính tổng quỹ lương phải trả)"""
        return sum(nv.luong_ht for nv in ds)


if __name__ == '__main__':
    print("\n Test: 1. Khởi tạo dữ liệu nhân viên")
    ds_nv = NhanVien.init_nv()
    print("\t+ Kết quả:", len(ds_nv), "nhân viên")

    print("\n Test: 2. In các nhân viên trong công ty")
    NhanVien.print_nv(ds_nv)

    print("\n Test: 3. Tính lương các nhân viên")
    for nv in ds_nv:
        nv.tinh_luong_ht()
    print("Kết quả: ")
    NhanVien.print_nv(ds_nv)

    print("\n Test: 4. Tìm nhân viên theo mã nhân viên")
    nv = NhanVien.tim_nv_theo_ma_nv(ds_nv, 104) #Có
    print("\t + Kết quả tìm: ", end="")
    if nv:
        nv.in_nv()

    nv = NhanVien.tim_nv_theo_ma_nv(ds_nv, 124)  # Không
    print("\t + Kết quả tìm: ", end="")
    if nv:
        nv.in_nv()
    else:
        print("Không tìm thấy nhân viên có mã 124")

    print("\n Test: 5. Cập nhật lương cơ bản theo mã nhân viên")
    nv = NhanVien.cap_nhat_luong_cb_theo_ma_nv(ds_nv,104, 5_000_000) #Có
    print("\t + Kết quả: ", end="")
    if nv:
        nv.in_nv()

    nv = NhanVien.cap_nhat_luong_cb_theo_ma_nv(ds_nv,124, 15_000_000) #Không
    print("\t + Kết quả: ", end="")
    if nv:
        nv.in_nv()
    else:
        print("Không tìm thấy nhân viên có mã 124")

    print("\n Test: 6. Tìm nhân viên có lương cao nhất")
    nv = NhanVien.tim_nv_co_luong_cao_nhat(ds_nv)
    print("\t + Kết quả: ", end="")
    if nv:
        nv.in_nv()

    print("\n Test: 7. Tìm nhân viên có số sản phẩm bán được thấp nhất")
    nv = NhanVien.tim_nv_co_so_sp_thap_nhat(ds_nv)
    print("\t + Kết quả: ", end="")
    if nv:
        nv.in_nv()

    print("\n Test: 8. Tìm 10 nhân viên có lương cao nhất")
    top_10_nv = NhanVien.tim_10_nv_co_luong_cao_nhat(ds_nv)
    print("\t + Kết quả: ")
    NhanVien.print_nv(top_10_nv)

    print("\n Test: 9. Sắp xếp nhân viên tăng dần theo lương hàng tháng")
    ds_sorted = NhanVien.sap_xep_nv_luong_ht_tang_dan(ds_nv)
    print("\t + Kết quả: ")
    NhanVien.print_nv(ds_sorted)

    print("\n Test: 10. Tự xây dựng thêm thao tác thích hợp cho bài toán (Xóa nhân viên theo mã nhân viên)")
    nv_1 = NhanVien.xoa_nv_theo_ma_nv(ds_nv, 116) #Có
    nv_2 = NhanVien.xoa_nv_theo_ma_nv(ds_nv, 126) #Không
    print("\t + Danh sách sau khi xóa: ")
    NhanVien.print_nv(ds_nv)

    print("\n Test: 10. Tự xây dựng thêm thao tác thích hợp cho bài toán (Tính tổng quỹ lương phải trả)")
    tong = NhanVien.tinh_tong_quy_luong_phai_tra(ds_nv)
    print(f"\t + Tổng tiền: {tong}")
