from debit import hitung_rata_rata, cari_terendah, cek_status

print("=== PENGUJIAN FUNGSI DEBIT ===")
print("Rata-rata [10, 20, 30]:", hitung_rata_rata([10, 20, 30]))
print("Terendah [12.5, 14.0, 11.0]:", cari_terendah([12.5, 14.0, 11.0]))

print("\n--- Pengujian Status Debit Otomatis ---")
daftar_uji = [9.9, 10.0, 20.0, 20.1]
for nilai in daftar_uji:
    status = cek_status(nilai)
    print(f"Nilai debit {nilai} -> Status: {status}")