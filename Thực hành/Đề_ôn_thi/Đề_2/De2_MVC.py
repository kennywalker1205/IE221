#Tạo MVC trong đó có controller: Khởi tạo dữ liệu -> Tính tiền -> In ra
from De2 import Phuong, Ho_GD, Ho_KD, Ho_SX

#Model
class Model:
    def __init__(self):
        self.phuong = Phuong('Phuong08', 'Linh Xuân')

    def load_data(self):
        self.phuong.init_ds_kh()

#View
class View:
    @classmethod
    def show_ds_kh(cls, ds):
        for kh in ds:
            print(kh)

#Controller
class Controller:
    def __init__(self, m: Model, v:View):
        self.m = m
        self.v = v

    def load_data_tinh_tien_dien_show(self):
        self.m.load_data() #1. Khởi tạo
        self.m.phuong.tinh_tien_dien() #2. Tính tiền điện
        self.v.show_ds_kh(self.m.phuong.get_ds()) #3. In ra kết quả

#--Test
if __name__ == '__main__':
    m = Model()
    v = View()
    c = Controller(m, v)

    print("\n Test: Khởi tạo dữ liệu nhân viên, tính tiền điện và in ra kết quả")
    c.load_data_tinh_tien_dien_show()

