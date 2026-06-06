class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self.__ma_nv = ma_nv
        self.__ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_ht = 0

    def get_ma_nv(self):
        return self.__ma_nv

    def set_ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv

    @property
    def ma_nv(self):
        return self.__ma_nv

    @ma_nv.setter
    def ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv

    def in_nv(self):
        print([self.__ma_nv,self.__ho_ten,self._luong_cb,self._luong_ht])

if __name__ == '__main__':
    nv = NhanVien(123, "Nguyễn Văn A", 3_000_000)
    nv.in_nv()

    # m = nv.get_ma_nv()
    # print(m)
    print(nv.ma_nv)

    # nv.set_ma_nv(123)
    nv.ma_nv = 123
    nv.in_nv()


