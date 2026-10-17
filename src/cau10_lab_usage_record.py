ma_phien = input("Nhap ma phien:")
ma_may = input("Nhap ma may:")
cong_suat = float(input("Nhap cong suat thiet bi (W):"))
so_phut = int(input("Nhap thoi gian su dung (phut):"))
don_gia = float(input("Nhap don gia dien (VND/kWh):"))
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
# dau ra
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat:.2f} W")
print(f"Thoi luong: {so_phut} phut")
print(f"Dien nang: {cong_suat * so_phut / 60 / 1000:.3f} kWh")
print(f"Chi phi: {(cong_suat * so_phut / 60 / 1000) * don_gia:.2f} VND")
print(f"Tren 60 phut: {so_phut > 60}")

print(f"Ghi nhan luc: {thoi_diem_text}")