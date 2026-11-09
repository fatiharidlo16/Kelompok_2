from lampu import Lampu

# Buat objek lp1 ("L1") dan lp2 ("L2")
lp1 = Lampu("L1")
lp2 = Lampu("L2")

# Nyalakan lp1 dan atur kecerahannya menjadi 60
lp1.nyalakan()
lp1.atur(60)

# Cetak lp1, lp2, dan Lampu.jumlah_lampu
print(lp1)
print(lp2)
print("Jumlah lampu:", Lampu.jumlah_lampu)