# Họ và tên: Phan Trung Kiên
# MSSV: 23520805
# Bài tập kéo búa bao (nâng cao)
import random as rd

diem_nguoi = 0
diem_may = 0
lan = 1
history = []

while diem_nguoi - diem_may != 2 or diem_may - diem_nguoi != 2:
    print("Lần ", lan)
    nguoi = input("Người ra: ")
    while nguoi not in ['kéo', 'búa', 'bao']: nguoi = input("Người nhập lại: ")
    print("Người đã ra: ", nguoi)
    may = rd.choice(['kéo', 'búa', 'bao'])
    print("Máy ra: ", may)

    if nguoi == may:
        diem_nguoi += 0.5
        diem_may += 0.5
        ket_qua = "Người hòa Máy"
    elif (nguoi == "kéo" and may == "bao") or (nguoi == "búa" and may == "kéo") or (nguoi == "bao" and may == "búa"):
        diem_nguoi += 1
        ket_qua = "Người thắng"
    else:
        diem_may += 1
        ket_qua = "Máy thắng"
    print("Kết quả: ", ket_qua)
    print("Điểm người: ", diem_nguoi, " | Điểm máy: ", diem_may)
    history.append((lan, nguoi, may, ket_qua))

    if diem_nguoi - diem_may == 2 or diem_may - diem_nguoi == 2: break
    lan += 1

#Tính chung cuộc
if diem_nguoi > diem_may: ket_qua_final = "Người thắng"
else: ket_qua_final = "Máy thắng"

print("Kết quả chung cuộc: ", ket_qua_final)

#Lịch sử chơi
print("Lịch sử chơi: ")
for i in history:
    print("Lần", i[0], ": Người:", i[1], ", Máy:", i[2], "=>", i[3])
