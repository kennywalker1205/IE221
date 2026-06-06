from abc import ABC, abstractmethod

#Nhan Vien
class AbcNhanVien(ABC):
    @abstractmethod
    def tinh_luong_ht(self):
        pass

class NhanVien(AbcNhanVien):
    def __init__(self, ma_nv, luong_cb, hs_tn):
        self._ma_nv = ma_nv
        self._luong_cb = luong_cb
        self._hs_tn = hs_tn
        self._luong_ht = 0

    @abstractmethod
    def tinh_luong_ht(self):
        pass

    def __str__(self):
        return str([self._ma_nv, self._luong_cb, self._hs_tn, self._luong_ht])

class ChuyenVien(NhanVien):
    def __init__(self, ma_nv, luong_cb, hs_tn, gio_tc):
        super().__init__(ma_nv, luong_cb, hs_tn)
        self.__gio_tc = gio_tc

    def tinh_luong_ht(self):
        self._luong_ht = self._luong_cb + (self._luong_cb * self._hs_tn) + (self.__gio_tc * 180000)
        return self._luong_ht

class NghienCuuVien(NhanVien):
    def __init__(self, ma_nv, luong_cb, hs_tn, so_pm):
        super().__init__(ma_nv, luong_cb, hs_tn)
        self.__so_pm = so_pm

    def tinh_luong_ht(self):
        self._luong_ht = self._luong_cb + (self._luong_cb * (self._hs_tn + 0.2)) + (self.__so_pm * 5500000)
        return self._luong_ht

class NVQuanLy(NhanVien):
    def __init__(self, ma_nv, luong_cb, hs_tn, hs_kn):
        super().__init__(ma_nv, luong_cb, hs_tn)
        self.__hs_kn = hs_kn

    def tinh_luong_ht(self):
        self._luong_ht = (self._luong_cb * 0.7) + (self._luong_cb * self._hs_tn) + (self._luong_cb * self.__hs_kn)
        return self._luong_ht

#Luong
class AbcLuong(ABC):
    @abstractmethod
    def init_ds_nv(self, data):
        pass

    @abstractmethod
    def tinh_luong_ht(self):
        pass

class Luong(AbcLuong):
    def __init__(self, ma_so):
        self.__ma_so = ma_so
        self.__ds = []

    """1. Tạo thông tin cho các nhân viên"""
    def init_ds_nv(self, data):
        self.__ds = data

    """2. Tính lương cho các nhân viên"""
    def tinh_luong_ht(self):
        for nv in self.__ds:
            nv.tinh_luong_ht()

    def get_ds(self):
        return self.__ds

    """3. Tìm kiếm nhân viên theo mã nhân viên"""
    def tim_nv_theo_ma_nv(self, ma_nv):
        for nv in self.__ds:
            if nv._ma_nv == ma_nv:
                return nv
        return None

    """4. Tổng số tiền phải trả cho các nhân viên"""
    def tong_tien_phai_tra_nv(self):
        return sum(nv._luong_ht for nv in self.__ds)

    """5. Tìm mã nhân viên đầu tiên có tổng lương lớn nhất"""
    def tim_nv_luong_ht_cao_nhat(self):
        if not self.__ds: return None
        return max(self.__ds, key=lambda nv: nv._luong_ht)

    """6. Cập nhật lại lương cơ bản theo mã nhân viên"""
    def cap_nhat_luong_cb_theo_ma_nv(self, ma_nv, luong_cb_new):
        nv = self.tim_nv_theo_ma_nv(ma_nv)
        if nv:
            nv._luong_cb = luong_cb_new
            nv.tinh_luong_ht()
            return True
        return False

    """7. Khởi tạo nhanh 6 nhân viên (Không dùng Input)"""
    def khoi_tao_nhanh_sau_nv(self):
        data = [
            ChuyenVien(126, 4500000, 0.5, 50),
            NghienCuuVien(127, 5600000, 1.2, 10),
            NVQuanLy(128, 7800000, 1.5, 1.3),
            NghienCuuVien(129, 8100000, 0.8, 12),
            NVQuanLy(130, 9500000, 1.0, 1.6),
            ChuyenVien(131, 6500000, 0.8, 30)
        ]
        self.init_ds_nv(data)