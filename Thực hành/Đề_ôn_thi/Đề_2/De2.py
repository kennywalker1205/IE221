#2350805_Phan Trung Kiên
from abc import ABC, abstractmethod

#Ho_Khach_Hang
class AbcHoKhachHang(ABC):
    loai1 = 3_500
    loai2 = 5_500
    loai3 = 7_000

    @abstractmethod
    def tinh_tien_dien(self):
        pass

class HoKhachHang(AbcHoKhachHang):
    def __init__(self, ma_kh, ten_ch, cs_cu, cs_moi):
        self._ma_kh = ma_kh
        self._ten_ch = ten_ch
        self._cs_cu = cs_cu
        self._cs_moi = cs_moi
        self._tien_dien = 0

    @abstractmethod
    def tinh_tien_dien(self):
        pass

    def __str__(self):
        loai_kh = self.__class__.__name__
        return f"{loai_kh} : Mã KH: {self._ma_kh} , Tên chủ hộ: {self._ten_ch} , cs cũ: {self._cs_cu} , cs moi: {self._cs_moi} , Tiền điện: {self._tien_dien}"

#Ho_Gia_Đinh
class Ho_GD(HoKhachHang):
    def __init__(self, ma_kh, ten_ch, cs_cu, cs_moi):
        super().__init__(ma_kh, ten_ch, cs_cu, cs_moi)

    def tinh_tien_dien(self):
        A = self._cs_moi - self._cs_cu
        if A > 100: tien_dien = A * AbcHoKhachHang.loai2
        else: tien_dien = A * AbcHoKhachHang.loai1

        self._tien_dien = tien_dien
        return tien_dien

#Ho_Kinh_Doanh
class Ho_KD(HoKhachHang):
    def __init__(self, ma_kh, ten_ch, cs_cu, cs_moi, hs_sd):
        super().__init__(ma_kh, ten_ch, cs_cu, cs_moi)
        self.__hs_sd = hs_sd

    def tinh_tien_dien(self):
        A = self._cs_moi - self._cs_cu
        if A > 500: tien_dien = A * AbcHoKhachHang.loai3 * self.__hs_sd
        else: tien_dien = A * AbcHoKhachHang.loai2 * self.__hs_sd

        self._tien_dien = tien_dien
        return tien_dien


# Ho_San_Xuat
class Ho_SX(HoKhachHang):
    def __init__(self, ma_kh, ten_ch, cs_cu, cs_moi, hs_sd):
        super().__init__(ma_kh, ten_ch, cs_cu, cs_moi)
        self.__hs_sd = hs_sd

    def tinh_tien_dien(self):
        A = self._cs_moi - self._cs_cu
        tien_dien = A * AbcHoKhachHang.loai3 * self.__hs_sd
        self._tien_dien = tien_dien

        return tien_dien

#Phuong
class AbcPhuong(ABC):
    @abstractmethod
    def init_ds_kh(self):
        pass

    @abstractmethod
    def tinh_tien_dien(self):
        pass

class Phuong(AbcPhuong):
    def __init__(self, ma_p, ten_p):
        self.__ma_p = ma_p
        self.__ten_p = ten_p
        self.__ds = []

    '''1. Khởi tạo nhanh 7 khách hàng có dữ liệu sau để kiểm tra chương trình'''
    def init_ds_kh(self):
        data = [
            Ho_KD(123, "A", 120, 960, 1.8),
            Ho_GD(124, "B", 400, 450),
            Ho_KD(125, "C", 300, 689, 1.3),
            Ho_SX(126, "D", 150, 965, 1.5),
            Ho_GD(127, "E", 500, 999),
            Ho_SX(128, "F", 350, 987, 1.6),
            Ho_SX(129, "G", 100, 989, 1.9),
        ]

        self.__ds = data
        return len(self.__ds)

    def get_ds(self):
        return self.__ds

    '''2. Thực hiện việc tính tiền điện cho từng khách hàng'''
    def tinh_tien_dien(self):
        for kh in self.__ds:
            kh.tinh_tien_dien()

    '''3. Tìm kiếm khách hàng theo mã khách hàng'''
    def tim_kh_theo_ma_kh(self, ma_kh):
        for kh in self.__ds:
            if kh._ma_kh == ma_kh:
                return kh
        return None

    '''4. Tính trung bình tiền điện của tất cả khách hàng trong Phường'''
    def tinh_tb_tien_dien(self):
        if not self.__ds:
            return 0
        tong_tien_dien = sum(kh._tien_dien for kh in self.__ds)
        return tong_tien_dien / len(self.__ds)

    '''5. Tìm khách hàng có số tiền điện lớn nhất'''
    def tim_kh_tien_dien_max(self):
        if not self.__ds: return None
        return max(self.__ds, key = lambda kh: kh._tien_dien)

    '''6. Tìm khách hàng loại hộ sản xuất có tiền điện nhỏ nhất'''
    def tim_kh_ho_sx_tien_dien_min(self):
        ds_kh_sx = [kh for kh in self.__ds if isinstance(kh, Ho_SX)]
        if not ds_kh_sx:
            return None
        return min(ds_kh_sx, key = lambda kh: kh._tien_dien)

    '''7. Viết hàm main, thiết kế các testcase kiểm tra các yêu cầu trên'''
#--Test
if __name__ == "__main__":
    print("\n Test: 1.Khởi tạo nhanh 7 khách hàng có dữ liệu")
    phuong = Phuong('P08', 'Linh Xuân')
    num = phuong.init_ds_kh()
    print(f"Đã tạo {num} khách hàng")

    print("\n Test: 2.Thực hiện việc tính tiền điện cho từng khách hàng")
    phuong.tinh_tien_dien()
    ds_kh = phuong.get_ds()
    for kh in ds_kh:
        print(kh)

    print("\n Test: 3.Tìm kiếm khách hàng theo mã khách hàng")
    #Có tìm thấy
    kh_can_tim = phuong.tim_kh_theo_ma_kh(126)
    if kh_can_tim:
        print(kh_can_tim)
    else:
        print(f"Không tìm thấy khách hàng có mã 126")

    #Không tìm thấy
    kh_can_tim_2 = phuong.tim_kh_theo_ma_kh(136)
    if kh_can_tim_2:
        print(kh_can_tim_2)
    else:
        print(f"\n Không tìm thấy khách hàng có mã 136")

    print("\n Test: 4. Tính trung bình tiền điện của tất cả khách hàng trong Phường")
    tien_dien_tb = phuong.tinh_tb_tien_dien()
    print(f"Tiền điện trung bình của Phường: {tien_dien_tb:.0f}")

    print("\n Test: 5. Tìm khách hàng có số tiền điện lớn nhất")
    kh_max = phuong.tim_kh_tien_dien_max()
    if kh_max:
        print(kh_max)

    print("\n Test: 6. Tìm khách hàng loại hộ sản xuất có tiền điện nhỏ nhất")
    kh_sx_min = phuong.tim_kh_ho_sx_tien_dien_min()
    if kh_sx_min:
        print(kh_sx_min)







