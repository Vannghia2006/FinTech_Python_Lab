# Nhập thông tin khách hàng
ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số CCCD: ")
so_tien_nap = float(input("Nhập số tiền nạp ban đầu (VND): "))

# Phí mở tài khoản
phi_mo_vi = 50000

# Tính số dư khả dụng
so_du = so_tien_nap - phi_mo_vi

# In biên lai
print("\n========== BIÊN LAI KHỞI TẠO VÍ ==========")
print(f"Họ tên: {ho_ten.upper()}")
print(f"Số điện thoại: {so_dien_thoai}")
print(f"4 số cuối CCCD: {cccd[-4:]}")
print(f"Số tiền nạp: {so_tien_nap:,.0f} VND")
print(f"Phí mở ví: {phi_mo_vi:,.0f} VND")
print(f"Số dư khả dụng: {so_du:,.0f} VND")
print("==========================================")
