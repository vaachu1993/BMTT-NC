so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
giotieuchuan = 44
giovuotchuan = max(0, so_gio_lam - giotieuchuan)
thuc_linh = giotieuchuan * luong_gio + giovuotchuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")