
from baca_log import baca_log
from galat import galat_absolut, galat_relatif, status
from statistik import rata_rata

valid, ditolak = baca_log("log_mikrofon.csv")

ACUAN = 62.4412

# Empat data pertama dan rata-rata data valid
pengujian = valid[:4] + [rata_rata(valid)]

for i, hasil in enumerate(pengujian, start=1):
    ga = galat_absolut(hasil, ACUAN)
    gr = galat_relatif(hasil, ACUAN)
    st = status(hasil, ACUAN)

    if i == 5:
        nama = "Rata-rata"
    else:
        nama = f"Data {i}"

    print(
        f"{nama}: hasil={hasil}, "
        f"galat absolut={ga:.4f}, "
        f"galat relatif={gr:.4f}%, status={st}"
    )
