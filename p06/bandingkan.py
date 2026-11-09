from baca_mentah import baca_mentah
from baca_log import baca_log
from statistik import rata_rata
from galat import galat_relatif, status

ACUAN_RATA = 62.4412

# 1. Tanpa validasi (baca mentah)
data_mentah = baca_mentah("log_mikrofon.csv")
rata_mentah = rata_rata(data_mentah)
galat_mentah = galat_relatif(rata_mentah, ACUAN_RATA)

# 2. Dengan validasi (baca bersih)
data_valid, _ = baca_log("log_mikrofon.csv")
rata_bersih = rata_rata(data_valid)
galat_bersih = galat_relatif(rata_bersih, ACUAN_RATA)

print(f"Rata-rata Mentah : {rata_mentah:.4f} | Galat: {galat_mentah:.2f}% | Status: {status(galat_mentah)}")
print(f"Rata-rata Bersih : {rata_bersih:.4f} | Galat: {galat_bersih:.4f}% | Status: {status(galat_bersih)}")