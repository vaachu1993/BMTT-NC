def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
so_nhi_phan = input("Nhập số nhị phân: ")  
if chia_het_cho_5(so_nhi_phan):
    print("Số nhị phân này chia hết cho 5")
else:
    print("Số nhị phân này không chia hết cho 5")