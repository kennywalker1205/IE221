from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class NhanVien(models.Model):
    ma_nv = models.IntegerField()
    ho_ten = models.CharField(max_length=200)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=10)
    dia_chi = models.CharField(max_length=500)
    def __str__(self):
        return str([self.ma_nv, self.ho_ten])