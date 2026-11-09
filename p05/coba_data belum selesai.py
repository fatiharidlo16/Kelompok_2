# Misal kita punya dictionary data ringkasan (r)
r = {"min": 10, "max": 50, "rata": 30}
print("Dictionary awal r:", r)

# 1. Menguji akses key yang tidak ada menggunakan key langsung r["median"]
try:
    print(r["median"])
except KeyError as e:
    print("Error r['median']:", e)

# 2. Menggunakan method r.get() untuk key yang tidak ada
print("Menggunakan r.get('median'):", r.get("median"))
print("Menggunakan r.get dengan default:", r.get("median", 0))

# 3. Menghitung panjang dictionary (len)
print("Panjang len(r):", len(r))

# 4. Mengubah / menambah isi dictionary & cek len setelah diubah
r["median"] = 28
r["rata"] = 32  # mengubah nilai yang sudah ada
print("Isi r setelah diubah:", r)
print("Panjang len(r) setelah diubah:", len(r))