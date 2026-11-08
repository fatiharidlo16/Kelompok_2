from audio import daftar_masukan, rekam, ke_level_db

print("Daftar perangkat input:")
daftar_masukan()

print("\nMerekam suara selama 2 detik...")
sinyal = rekam(2)

print("Jumlah sampel:", len(sinyal))
print("Level suara:", round(ke_level_db(sinyal), 2), "dB")