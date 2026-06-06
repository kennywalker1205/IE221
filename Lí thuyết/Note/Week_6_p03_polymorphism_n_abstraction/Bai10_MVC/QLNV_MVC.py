from QLNV_Luong import CongTy


class View:
    @classmethod
    def show(cls, ds):
        for item in ds:
            item.in_nv()  # Đã bỏ print() bọc ngoài để tránh in ra None


class Model:
    def __init__(self):
        self.ct = CongTy("Thang 03")


class Controller:
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view

    def tinh_luong_ht(self):
        """Triển khai quy trình tính lương"""
        # 1. Lấy dữ liệu nv
        self.__model.ct.init_ds_nv()  # Đã sửa: self.__model và init_ds_nv()

        # 2. Gọi cách tính lương
        self.__model.ct.tinh_luong_ht()  # Đã sửa: self.__model và bỏ chữ .init thừa

        # 3. Hiển thị ra
        self.__view.show(self.__model.ct.get_ds_nv())  # Đã sửa: self.__view và self.__model

        # 4. Lưu trữ (nếu có)


if __name__ == '__main__':
    v = View()
    model = Model()
    controller = Controller(model, v)

    controller.tinh_luong_ht()