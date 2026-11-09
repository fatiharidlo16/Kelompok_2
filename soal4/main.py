from perangkat import SensorSuhu, SensorDebit

# 1. Buat objek SensorSuhu dan SensorDebit
suhu = SensorSuhu("Suhu")
debit = SensorDebit("Debit", "L/menit")

# 2. Isi data sensor suhu
suhu.baca(30.1)
suhu.baca(30.6)
suhu.baca(30.3)

# 3. Isi data sensor debit
debit.baca(12.0)
debit.baca(15.0)
debit.baca(15.0)

# 4. Masukkan keduanya ke satu list dan jalankan perulangan
perangkat_list = [suhu, debit]

for p in perangkat_list:
    print(f"{p.nama} -> {p.proses()}")