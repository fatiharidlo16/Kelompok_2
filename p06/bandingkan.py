
from baca_mentah import baca_mentah
from baca_log import baca_log
from galat import galat_relatif
from validasi import dalam_rentang
from statistik import rata_rata

ACUAN = 62.4412

# Data tanpa validasi
mentah = baca_mentah("log_mikrofon.csv")

# Data setelah validasi
valid, ditolak = baca_log("log_mikrofon.csv")

# Hitung rata-rata dan galat
rata_mentah = rata_rata(mentah)
rata_valid = rata_rata(valid)

print("=== TANPA VALIDASI ===")
print("Jumlah data:", len(mentah))
print("Rata-rata:", rata_mentah)

try:
    print("Galat relatif:", galat_relatif(rata_mentah, ACUAN), "%")
    print("Output wajar:", dalam_rentang(rata_mentah))
except ValueError as e:
    print("Error:", e)

print("\n=== SETELAH VALIDASI ===")
print("Jumlah data valid:", len(valid))
print("Jumlah data ditolak:", len(ditolak))
print("Rata-rata:", rata_valid)

try:
    print("Galat relatif:", galat_relatif(rata_valid, ACUAN), "%")
    print("Output wajar:", dalam_rentang(rata_valid))
except ValueError as e:
    print("Error:", e)
