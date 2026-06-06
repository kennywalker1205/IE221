from De1 import *

#Model
class Model:
    def __init__(self):
        self.daily = DaiLy()

    def load_data(self):
        self.daily.init_ds_nv()

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

    def load_data_tinh_luong_show(self):
        self.m.load_data()
        self.m.daily.tinh_luong()
        self.v.show_ds_nv(self.m.daily.get_ds())

#--Test
if __name__ == '__main__':
    m = Model()
    v = View()
    c = Controller(m, v)

    print("\n Test: Khởi tạo dữ liệu, tính lương và in ra kết quả")
    c.load_data_tinh_luong_show()