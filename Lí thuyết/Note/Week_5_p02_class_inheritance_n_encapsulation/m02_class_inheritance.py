class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.luong_ht = 0

class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ng):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_ng = so_ng

    def in_nv_vp(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_ng])

    def tinh_luong_ht_nv_vp(self):
        luong = self.luong_cb + self.so_ng * 150_000
        self.luong_ht += luong
        return luong

class NVBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_sp = so_sp

    def in_nv_bh(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_sp])

    def tinh_luong_ht_nv_bh(self):
        luong = self.luong_cb + self.so_sp * 18_000
        self.luong_ht += luong
        return luong

class CongTy:
    def __init__(self, ma_ct, ):
        self.ma_ct = ma_ct
        self.ds = []

    def init_ds_nv(self):
        """1. Khởi tạo dữ liệu nhân viên"""
        vp1 = NVVanPhong(123, 'Nguyễn Văn A', 5_600_000, 23)
        vp2 = NVVanPhong(385, 'Nguyễn Thụy D', 7_800_000, 25)
        bh1 = NVBanHang(456, 'Phan Văn B', 3_900_000, 70)
        bh2 = NVBanHang(789, 'Phan Lệ C', 3_900_000, 85)
        self.ds.extend([vp1, vp2, bh1, bh2])

        return len(self.ds)

    def print_ds_nv(self):
        """2. In danh sách các nhân viên trong công ty"""
        for nv in self.ds:
            if isinstance(nv, NVVanPhong):
                nv.in_nv_vp()
            elif isinstance(nv, NVBanHang):
                nv.in_nv_bh()

    def tinh_luong_ht(self):
        """3. Tính lương hàng tháng"""
        for nv in self.ds:
            if isinstance(nv, NVVanPhong):
                nv.tinh_luong_ht_nv_vp()
            elif isinstance(nv, NVBanHang):
                nv.tinh_luong_ht_nv_bh()

    def tim_nv_theo_ma_nv(self, ma_nv):
        """4. Tìm nhân viên theo mã nhân viên"""
        # version 1
        for nv in self.ds:
            if nv.ma_nv == ma_nv:
                return nv

    def tim_nv_theo_ma_nv_V2(self, ma_nv):
        # version 2
        f = filter(lambda nv: nv.ma_nv == ma_nv, self.ds)
        return list(f)

    def tim_nv_luong_ht_cao_nhat(self):
        """5. Tìm nhân viên có lương hàng tháng cao nhất"""
        nv_max = max(self.ds, key = lambda nv: nv.luong_ht)
        return nv_max

    def tim_nv_luong_ht_cao_nhat_V2(self):
        max_luong_ht = 0
        for nv in self.ds:
            if nv.luong_ht > max_luong_ht:
                max_luong_ht = nv.luong_ht
        return max_luong_ht

    def tim_nv_bh_luong_ht_thap_nhat(self):
        """6. Tìm nhân viên bán hàng có lương hàng tháng thấp nhất"""
        ds_nv_bh = list(filter(lambda nv: isinstance(nv, NVBanHang), self.ds))

        nv_min = min(ds_nv_bh, key = lambda nv: nv.luong_ht)
        return nv_min

    def sap_xep_luong_ht_giam_dan(self):
        """7. Sắp xếp nhân viên có lương hằng tháng giảm dần"""
        self.ds.sort(key = lambda nv: nv.luong_ht, reverse = True)

if __name__ == '__main__':
    print("Test: 1. Khởi tạo dữ liệu nhân viên")
    ct = CongTy('UIT-GSC')
    so_nv = ct.init_ds_nv()
    print("\t+ Kết quả:", so_nv, "nhân viên")

    print("\n Test: 2. In danh sách các nhân viên trong công ty")
    ct.print_ds_nv()

    print("\n Test: 3. Tính lương hàng tháng")
    ct.tinh_luong_ht()
    print("Kết quả: ")
    ct.print_ds_nv()

    print("\n Test: 4. Tìm nhân viên theo mã nhân viên")
    nv = ct.tim_nv_theo_ma_nv(123) #Có
    print("\t + Kết quả tìm: ", end = "")
    if isinstance(nv, NVVanPhong):
        nv.in_nv_vp()
    elif isinstance(nv, NVBanHang):
        nv.in_nv_bh()

    nv = ct.tim_nv_theo_ma_nv(124) #Không
    print("\t + Kết quả tìm: ", end="")
    if isinstance(nv, NVVanPhong):
        nv.in_nv_vp()
    elif isinstance(nv, NVBanHang):
        nv.in_nv_bh()

    print("\n Test: 4.v2 Tìm nhân viên theo mã nhân viên")
    nv = ct.tim_nv_theo_ma_nv_V2(123)  # Có
    print("\t + Kết quả tìm: ", end="")
    if nv:
        for nv_V2 in nv:
            if isinstance(nv_V2, NVVanPhong):
                nv_V2.in_nv_vp()
            elif isinstance(nv_V2, NVBanHang):
                nv_V2.in_nv_bh()

    nv = ct.tim_nv_theo_ma_nv_V2(124)  # Không
    print("\t + Kết quả tìm: ", end="")
    if nv:
        for nv_V2 in nv:
            if isinstance(nv_V2, NVVanPhong):
                nv_V2.in_nv_vp()
            elif isinstance(nv_V2, NVBanHang):
                nv_V2.in_nv_bh()

    print("\n Test: 5. Tìm nhân viên có lương hàng tháng cao nhất")
    nv = ct.tim_nv_luong_ht_cao_nhat()
    if nv:
        print("\t + Kết quả tìm: ", end="")
        if isinstance(nv, NVVanPhong):
            nv.in_nv_vp()
        elif isinstance(nv, NVBanHang):
            nv.in_nv_bh()

    print("\n Test: 6. Tìm nhân viên bán hàng có lương hàng tháng thấp nhất")
    nv = ct.tim_nv_bh_luong_ht_thap_nhat()
    if nv:
        print("\t + Kết quả tìm: ", end="")
        if isinstance(nv, NVVanPhong):
            nv.in_nv_vp()
        elif isinstance(nv, NVBanHang):
            nv.in_nv_bh()

    print("\n Test: 7. Sắp xếp nhân viên có lương theo tháng giảm dần")
    ct.sap_xep_luong_ht_giam_dan()
    print("\t + Kết quả: ")
    ct.print_ds_nv()




