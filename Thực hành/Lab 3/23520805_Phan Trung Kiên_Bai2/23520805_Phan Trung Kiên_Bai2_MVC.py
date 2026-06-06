from Bai2 import Luong, NVQuanLy, ChuyenVien, NghienCuuVien

#Model
class Model:
    def __init__(self):
        self.luong = Luong('Thang04')

    def load_data(self):
        data = [
            NVQuanLy(123, 9_200_000, 2.5, 1.2),  # Truyền: ma_nv, luong_cb, hs_tn, hs_kn
            ChuyenVien(124, 9_200_000, 2.5, 230),  # Truyền: ma_nv, luong_cb, hs_tn, gio_tc
            NghienCuuVien(125, 9_200_000, 2.5, 2)  # Truyền: ma_nv, luong_cb, hs_tn, so_pm
        ]

        self.luong.init_ds_nv(data)

#View
class View:
    @classmethod
    def show_ds_nv(cls, ds):
        for nv in ds:
            print(nv)

#Controller
class Controller:
    def __init__(self, m: Model, v: View):
        self.m = m
        self.v = v

    def load_data_tinh_luong_ht_show(self):
        self.m.load_data()
        self.m.luong.tinh_luong_ht()
        self.v.show_ds_nv(self.m.luong.get_ds())

    def load_data_tim_nv_theo_ma_nv(self, ma_nv):
        nv = self.m.luong.tim_nv_theo_ma_nv(ma_nv)
        if nv:
            self.v.show_ds_nv([nv])
        else:
            print(f"Không tìm thấy nhân viên có mã {ma_nv}")

    def load_data_tong_tien_phai_tra_nv(self):
        tong = self.m.luong.tong_tien_phai_tra_nv()
        print(f"Tổng số tiền phải trả: {tong}")

    def load_data_tim_nv_luong_ht_cao_nhat(self):
        nv_max = self.m.luong.tim_nv_luong_ht_cao_nhat()
        if nv_max:
            self.v.show_ds_nv([nv_max])

    def load_data_cap_nhat_luong_cb_theo_ma_nv(self, ma_nv, luong_cb_new):
        if self.m.luong.cap_nhat_luong_cb_theo_ma_nv(ma_nv, luong_cb_new):
            self.v.show_ds_nv([self.m.luong.tim_nv_theo_ma_nv(ma_nv)])
        else:
            print(f"Không tìm thấy nhân viên có mã {ma_nv}")

    def load_data_khoi_tao_nhanh_sau_nv(self):
        self.m.luong.khoi_tao_nhanh_sau_nv()
        self.m.luong.tinh_luong_ht()
        self.v.show_ds_nv(self.m.luong.get_ds())

#--Test
if __name__ == '__main__':
    m = Model()
    v = View()
    c = Controller(m, v)

    print("\n Test: 1 + 2. Tính lương và xuất thông tin từng nhân viên")
    c.load_data_tinh_luong_ht_show()

    print("\n Test: 3. Tìm nhân viên theo mã nhân viên")
    c.load_data_tim_nv_theo_ma_nv(124)
    c.load_data_tim_nv_theo_ma_nv(133)

    print("\n Test: 4. Tổng số tiền phải trả cho tất cả nhân viên")
    c.load_data_tong_tien_phai_tra_nv()

    print("\n Test: 5. Tìm nhân viên bán hàng có lương hàng tháng cao nhất")
    c.load_data_tim_nv_luong_ht_cao_nhat()

    print("\n Test: 6. Cập nhật lại lương cb nhân viên theo mã nhân viên")
    c.load_data_cap_nhat_luong_cb_theo_ma_nv(123, 10_200_000)
    c.load_data_cap_nhat_luong_cb_theo_ma_nv(133, 10_200_000)

    print("\n Test: 7. Khởi tạo nhanh 6 nhân viên (ko dùng input)")
    c.load_data_khoi_tao_nhanh_sau_nv()