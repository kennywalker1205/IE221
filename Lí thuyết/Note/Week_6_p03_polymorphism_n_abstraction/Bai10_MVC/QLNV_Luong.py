from abc import ABC, abstractmethod

class ABCNhanVien(ABC): # Đã thêm kế thừa (ABC) để sử dụng abstractmethod
    @abstractmethod
    def tinh_luong_ht(self):
        pass

class NhanVien(ABCNhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.luong_ht = 0

    def in_nv(self):
        # Đã sửa lại các thuộc tính cho đúng với hàm __init__ bên trên
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht])


class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ng):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_ng = so_ng

    def in_nv(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_ng])

    def tinh_luong_ht(self):
        luong = self.luong_cb + self.so_ng * 150_000

        self.luong_ht += luong
        return luong

class NVBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_sp = so_sp

    def in_nv(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_sp])

    def tinh_luong_ht(self):
        luong = self.luong_cb + self.so_sp * 18_000
        self.luong_ht += luong
        return luong

class CongTy:
    def __init__(self, ma_ct, ):
        self.ma_ct = ma_ct
        self.__ds = []

    def get_ds_nv(self):
        return self.__ds # Đã thêm self.__ds để trả về danh sách

    def init_ds_nv(self):
        """1. Khởi tạo dữ liệu nhân viên"""
        vp1 = NVVanPhong(123, 'Nguyễn Văn A', 5_600_000, 23)
        vp2 = NVVanPhong(385, 'Nguyễn Thụy D', 7_800_000, 25)
        bh1 = NVBanHang(456, 'Phan Văn B', 3_900_000, 70)
        bh2 = NVBanHang(789, 'Phan Lệ C', 3_900_000, 85)
        self.__ds.extend([vp1, vp2, bh1, bh2]) # Đổi self.ds thành self.__ds

        return len(self.__ds)

    def print_ds_nv(self):
        """2. In danh sách các nhân viên trong công ty"""
        list(map(lambda nv: nv.in_nv(), self.__ds))
        # for nv in self.__ds:
        #     nv.in_nv()
            #if isinstance(nv, NVVanPhong):
                #nv.in_nv_vp()
            #elif isinstance(nv, NVBanHang):
                #nv.in_nv_bh()

    def tinh_luong_ht(self):
        """3. Tính lương hàng tháng"""
        list(map(lambda nv: nv.tinh_luong_ht(), self.__ds))
        # for nv in self.__ds:
        #     nv.tinh_luong_ht()
            # if isinstance(nv, NVVanPhong):
            #     nv.tinh_luong_ht_nv_vp()
            # elif isinstance(nv, NVBanHang):
            #     nv.tinh_luong_ht_nv_bh()

    def tim_nv_theo_ma_nv(self, ma_nv):
        """4. Tìm nhân viên theo mã nhân viên"""
        # version 1
        for nv in self.__ds: # Đổi self.ds thành self.__ds
            if nv.ma_nv == ma_nv:
                return nv

    def tim_nv_theo_ma_nv_V2(self, ma_nv):
        # version 2
        f = filter(lambda nv: nv.ma_nv == ma_nv, self.__ds)
        return list(f)

    def tim_nv_luong_ht_cao_nhat(self):
        """5. Tìm nhân viên có lương hàng tháng cao nhất"""
        nv_max = max(self.__ds, key = lambda nv: nv.luong_ht)
        return nv_max

    def tim_nv_luong_ht_cao_nhat_V2(self):
        max_luong_ht = 0
        for nv in self.__ds:
            if nv.luong_ht > max_luong_ht:
                max_luong_ht = nv.luong_ht
        return max_luong_ht

    def tim_nv_bh_luong_ht_thap_nhat(self):
        """6. Tìm nhân viên bán hàng có lương hàng tháng thấp nhất"""
        ds_nv_bh = list(filter(lambda nv: isinstance(nv, NVBanHang), self.__ds)) # Đổi self.ds thành self.__ds

        nv_min = min(ds_nv_bh, key = lambda nv: nv.luong_ht)
        return nv_min

    def sap_xep_luong_ht_giam_dan(self):
        """7. Sắp xếp nhân viên có lương hằng tháng giảm dần"""
        self.__ds.sort(key = lambda nv: nv.luong_ht, reverse = True) # Đổi self.ds thành self.__ds