ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá (VND): "))

# Tính tổng tiền hàng
tong_tien_hang = so_luong * don_gia

# Tính VAT 8%
vat = tong_tien_hang * 0.08

# Tính tổng thanh toán
tong_thanh_toan = tong_tien_hang + vat

# In hóa đơn
print("\n========== HÓA ĐƠN BÁN HÀNG ==========")
print(f"Tên sản phẩm: {ten_san_pham}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia:,.0f} VND")
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f} VND")
print(f"Thuế VAT (8%): {vat:,.0f} VND")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VND")
print("=======================================")
