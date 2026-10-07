# Bài tập 1: Masking Email khách hàng

email = input("Nhập địa chỉ email: ")

# Tách tên đăng nhập và tên miền
username, domain = email.split("@")

# Lấy 3 ký tự đầu tiên
first_3 = username[0:3]

# Ghép chuỗi
masked_email = first_3 + "***@" + domain

# In kết quả
print("Email sau khi che:", masked_email)

