# Bài tập 2: Máy quét sinh Mã ưu đãi

ho_ten = input("Nhập họ tên: ")
nam_sinh = input("Nhập năm sinh: ")

# Lấy tên cuối cùng
ten = ho_ten.split()[-1]

# Lấy 3 ký tự đầu và viết hoa
ma_ten = ten[0:3].upper()

# Tạo mã ưu đãi
ma_uu_dai = f"{ma_ten}-{nam_sinh}-VIP"

print("Mã ưu đãi:", ma_uu_dai)
