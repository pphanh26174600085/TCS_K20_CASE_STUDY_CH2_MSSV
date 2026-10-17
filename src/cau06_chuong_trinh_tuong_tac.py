ma_phien = input("Nhap ma phien:")
ma_may = input("Nhap ma may:")
cong_suat = float(input("Nhap cong suat:"))
so_phut = int(input("Nhap so phut su dung:"))
don_gia = float(input("Nhap don gia:"))

# tinh 
dien_nang = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia
print("Dien nang tieu thu la",dien_nang,"kWh")
print("Chi phi la",chi_phi,"dong")