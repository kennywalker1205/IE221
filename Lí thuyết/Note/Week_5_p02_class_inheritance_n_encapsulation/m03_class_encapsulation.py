class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_ht = 0

class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ng):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_ng = so_ng

    def in_nv_vp(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_ng])

class NVBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_sp = so_sp

    def in_nv_bh(self):
        print([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_sp])

class CongTy:
    def __init__(self, ma_ct, ten_ct, ds):
        self.__ma_ct = ma_ct
        self.__ten_ct = ten_ct
        self.__ds = []

if __name__ == '__main__':
    nv = NhanVien(123, "Nguyễn Văn A", 3_000_000)
    nv._ho_ten
    nv._ma_nv