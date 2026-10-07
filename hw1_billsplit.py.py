# hw1_billsplit.py

X = float(input("Nhập tổng hóa đơn: "))
Y = float(input("Nhập phần trăm tiền tip (%): "))
N = int(input("Nhập số người: "))

tien_tip = X * Y / 100
tong_tien = X + tien_tip
tien_moi_nguoi = tong_tien / N

print(f"Mỗi người phải trả: {tien_moi_nguoi:.0f} đồng")
