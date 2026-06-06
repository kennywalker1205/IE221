class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self.__ma_nv = ma_nv
        self.__ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_ht = 0

    def __str__(self):
        return str([self.__ma_nv, self.__ho_ten, self._luong_cb, self._luong_ht])

    def in_nv(self):
        print([self.__ma_nv, self.__ho_ten, self._luong_cb, self._luong_ht])

if __name__ == '__main__':
    nv = NhanVien(123, 'Nguyễn Văn A', 7_000_000)
    print(nv)
