ma_may = input("Nhap ma may:")
cong_suat_w = input("Nhap cong suat:")
so_phut = input("Nhap so phut su dung:")
don_gia = input("Nhap don gia dien:")

# in type() cua 4 bien
print(type(ma_may))
print(type(cong_suat_w))
print(type(so_phut))
print(type(don_gia))

# chuyen kieu du lieu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia = float(don_gia)

# tinh dien nang va chi phi
dien_nang = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia
print("Dien nang tieu thu la",dien_nang,"kWh")
print("Chi phi la",chi_phi,"dong")