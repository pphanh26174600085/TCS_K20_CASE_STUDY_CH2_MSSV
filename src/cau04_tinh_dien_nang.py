cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# tinhs dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print("Dien nang tieu thu =",dien_nang_kwh,",",type(dien_nang_kwh))
chi_phi = dien_nang_kwh * don_gia_kwh
print("Chi phi dien =",chi_phi,",",type(chi_phi))
# du doan
# 1. Dien nang tieu thu = 0.375, kieu du lieu la: float
# 2. Chi phi dien = 1125, kieu du lieu la: int

# thay so phut thanh 60
so_phut = 60
dien_nang_kwh_2 = cong_suat_w * so_phut / 60 / 1000
chi_phi_2 = dien_nang_kwh_2 * don_gia_kwh
print("Dien nang tieu thu moi =",dien_nang_kwh_2,",",type(dien_nang_kwh_2))
print("Chi phi dien moi =",chi_phi_2,",",type(chi_phi_2))

# so sanh
so_sanh_dien_nang = dien_nang_kwh > dien_nang_kwh_2
print(so_sanh_dien_nang)
so_sanh_chi_phi = chi_phi > chi_phi_2
print(so_sanh_chi_phi)