from abc import ABC, abstractmethod

#NhanVien
class AbcNhanVien(ABC):
    @abstractmethod
    def tinh_luong(self):
        pass

class NhanVien(AbcNhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_ht = 0

    @abstractmethod
    def tinh_luong(self):
        pass

    def __str__(self):
        loai_nv = self.__class__.__name__
        return f"{loai_nv} : Mã NV: {self._ma_nv} , Họ Tên: {self._ho_ten}, Lương CB: {self._luong_cb}, Lương HT: {self._luong_ht}"

#NVVanPhong
class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_gio):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_gio = so_gio

    def tinh_luong(self):
        if self.__so_gio > 100:
            luong = self._luong_cb + self.__so_gio * 220_000 + 5_000_000
        else: luong = self._luong_cb + self.__so_gio * 220_000

        self._luong_ht = luong

        return luong

#NVSanXuat
class NVSanXuat(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_sp = so_sp

    def tinh_luong(self):
        luong = self._luong_cb + self.__so_sp * 175_000
        if self.__so_sp > 150:
            luong += (luong * 0.2)

        self._luong_ht = luong
        return luong

#NVQuanLy
class NVQuanLy(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, hs_cv, thuong):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__hs_cv = hs_cv
        self.__thuong = thuong

    def tinh_luong(self):
        luong = self._luong_cb * self.__hs_cv + self.__thuong
        self._luong_ht = luong

        return luong

#DaiLy
class AbcDaiLy(ABC):
    @abstractmethod
    def init_ds_nv(self):
        pass

    @abstractmethod
    def tinh_luong(self):
        pass

class DaiLy(AbcDaiLy):
    def __init__(self):
        self.__ds = []

    '''1. Khởi tạo dữ liệu'''
    def init_ds_nv(self):
        data = [
            NVVanPhong(101, 'Nguyễn A', 4_500_000, 200),
            NVVanPhong(102, 'Nguyễn B', 5_600_000, 100),
            NVVanPhong(103, 'Nguyễn C', 8_900_000, 90),

            NVSanXuat(201, 'Nguyễn D', 7_800_000, 250),
            NVSanXuat(202, 'Nguyễn E', 4_500_000, 110),
            NVSanXuat(203, 'Nguyễn F', 6_600_000, 360),

            NVQuanLy(301, 'Nguyễn G', 8_500_000, 1.3, 19_500_000),
            NVQuanLy(302, 'Nguyễn H', 7_600_000, 1.2, 18_600_000),
        ]

        self.__ds = data
        return len(self.__ds)

    def get_ds(self):
        return self.__ds

    '''3. Tính lương cho từng nhân viên'''
    def tinh_luong(self):
        for nv in self.__ds:
            nv.tinh_luong()

    '''4. Tìm kiếm nhân viên theo mã nhân viên'''
    def tim_nv_theo_ma_nv(self, ma_nv):
        for nv in self.__ds:
            if nv._ma_nv == ma_nv:
                return nv
        return None

    '''5. Tính trung bình lương ht'''
    def tinh_trung_binh_luong_ht(self):
        if not self.__ds:
            return 0
        tong_tien_luong = sum(nv._luong_ht for nv in self.__ds)
        return tong_tien_luong / len(self.__ds)

    '''6. Cập nhật lương cb theo mã nv'''
    def cap_nhat_luong_cb(self, ma_nv, luong_cb_moi):
        nv = self.tim_nv_theo_ma_nv(ma_nv)

        if nv is not None:
            nv._luong_cb = luong_cb_moi
            nv.tinh_luong()
            return True

        return False

    '''7. Tìm nhân viên sản xuất có lương cao nhất'''
    def tim_nv_sx_luong_max(self):
        ds_nv_sx = [nv for nv in self.__ds if isinstance(nv, NVSanXuat)]
        if not ds_nv_sx:
            return None
        return max(ds_nv_sx, key = lambda nv: nv._luong_ht)

    '''8. Tìm nhân viên có lương cb thấp nhất'''
    def tim_nv_luong_cb_min(self):
        if not self.__ds: return None
        return min(self.__ds, key = lambda nv: nv._luong_ht)

    '''9. Viết hàm main, thiết kế testcase kiểm tra các yêu cầu'''
#--Test
if __name__ == '__main__':
    print("\n Test 1.")
    daily = DaiLy()
    num = daily.init_ds_nv()
    print(f"Đã tạo {num} nhân viên")

    print("\n Test 2.")
    ds_nv = daily.get_ds()
    for nv in ds_nv:
        print(nv)

    print("\n Test 3.")
    daily.tinh_luong()
    ds_nv = daily.get_ds()
    for nv in ds_nv:
        print(nv)

    print("\n Test 4.")
    #Có
    nv_can_tim = daily.tim_nv_theo_ma_nv(301)
    if nv_can_tim:
        print(nv_can_tim)
    else:
        print("Không tìm thấy nhân viên có mã tương ứng")

    #Không
    nv_can_tim = daily.tim_nv_theo_ma_nv(303)
    if nv_can_tim:
        print(nv_can_tim)
    else:
        print("Không tìm thấy nhân viên có mã tương ứng")

    print("\n Test 5.")
    tien_luong_tb = daily.tinh_trung_binh_luong_ht()
    print(f"Trung bình tiền lương hàng tháng đại lý trả cho nhân viên: {tien_luong_tb:.0f}")

    print("\n Test 6.")
    ma_nv = 101
    luong_cb_moi = 10_000_000

    print("\t Trước khi cập nhật:")
    print(daily.tim_nv_theo_ma_nv(101))
    print("\n Sau khi cập nhật:")
    update = daily.cap_nhat_luong_cb(101, 10_000_000)
    if update:
        print(daily.tim_nv_theo_ma_nv(101))
        
    print("\n Test 7.")
    nv_sx_max = daily.tim_nv_sx_luong_max()
    if nv_sx_max:
        print(nv_sx_max)

    print("\n Test 8.")
    nv_luong_cb_min = daily.tim_nv_luong_cb_min()
    if nv_luong_cb_min:
        print(nv_luong_cb_min)
        
