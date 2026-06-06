# Bài 8: OOP
class NhanVien:
    so_nv = 0 # Thuộc tính của Class
    # Khai báo đối tượng (Tên, thuộc tính)
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ngay):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.so_ngay = so_ngay
        self.luong_ht = 0

        NhanVien.so_nv += 1
    # Định nghĩa phương thức (Đối tượng)
    def in_nv(self):
        print(f"Mã NV: {self.ma_nv}\tHọ tên: {self.ho_ten}\tLương CB: {self.luong_cb}\tSố ngày làm việc: {self.so_ngay}\tLương hàng tháng: {self.luong_ht}")
        #print([self.ma_nv, self.ho_ten, self.luong_cb, self.so_ngay])

    def tinh_luong_ht(self):
        luong = (self.so_ngay * 150_000) + self.luong_cb
        self.luong_ht = luong
        return luong

    @classmethod #Định nghĩa phương thức của Class (áp dụng cho 1 hàm sau đó)
    def so_luong_nv(cls):
        return cls.so_nv

    @staticmethod #Phương thức không liên quan đến Class / Object (Phương thức tạm trú)
    def tinh_thue_tncn(tien):
        return tien*0.1

    # Khởi tạo đối tượng - Constructor
if __name__ == '__main__':
    nv1 = NhanVien(123, 'Nguyễn Văn A', 3_000_000, 23)
    nv2 = NhanVien(124, 'Nguyễn Văn B', 5_000_000, 22)

    # 3 cách gọi
    print(nv1.so_nv)
    print(nv2.so_nv)
    print(NhanVien.so_nv)

    nv2.tinh_thue_tncn(678935)
    NhanVien.tinh_thue_tncn(678935)

