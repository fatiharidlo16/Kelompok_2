from lampu import Lampu

# 1. Buat objek Lampu("L1")
l1 = Lampu("L1")
print("Awal:", l1.aktif, l1.kecerahan)

# 2. Nyalakan lampu
l1.nyalakan()
print("Setelah nyalakan():", l1.aktif, l1.kecerahan)

# 3. Baca tiga nilai kecerahan dengan input() (masukkan: 60, 150, -5)
val1 = float(input("Masukkan nilai ke-1 (60): "))
l1.atur(val1)
print(f"Setelah atur({val1}):", l1.aktif, l1.kecerahan)

val2 = float(input("Masukkan nilai ke-2 (150): "))
l1.atur(val2)
print(f"Setelah atur({val2}):", l1.aktif, l1.kecerahan)

val3 = float(input("Masukkan nilai ke-3 (-5): "))
l1.atur(val3)
print(f"Setelah atur({val3}):", l1.aktif, l1.kecerahan)

# 4. Matikan lampu
l1.matikan()
print("Setelah matikan():", l1.aktif, l1.kecerahan)