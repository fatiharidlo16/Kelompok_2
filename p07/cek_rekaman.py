from baca_log import baca_log, hitung_alasan
from statistik import ringkasan

valid, ditolak = baca_log("log_rekam.csv")

print("=== HASIL PEMERIKSAAN REKAMAN ===")
print("Jumlah data valid:", len(valid))
print("Jumlah data ditolak:", len(ditolak))

if valid:
    hasil = ringkasan(valid)

    print("\n=== STATISTIK DATA VALID ===")
    print("Jumlah:", hasil["jumlah"])
    print("Rata-rata:", hasil["rata"], "dB")
    print("Terendah:", hasil["min"], "dB")
    print("Tertinggi:", hasil["maks"], "dB")
    print("Median:", hasil["median"], "dB")

print("\n=== DATA YANG DITOLAK ===")
for no, isi, alasan in ditolak:
    print(f"Baris {no}: {isi} -> {alasan}")

print("\n=== JUMLAH BERDASARKAN ALASAN ===")
for alasan, jumlah in hitung_alasan(ditolak).items():
    print(f"{alasan}: {jumlah}")