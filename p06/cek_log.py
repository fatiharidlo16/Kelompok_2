from validasi import periksa

def baca_log(nama_berkas):
    valid = []
    ditolak = []
    with open(nama_berkas) as berkas:
        next(berkas)  # Lewati baris header/judul kolom
        for no, baris in enumerate(berkas, start=2):
            baris = baris.strip()
            kolom = baris.split(",")
            if len(kolom) != 2:
                ditolak.append((no, baris, "jumlah kolom salah"))
                continue
            try:
                valid.append(periksa(kolom[1]))
            except ValueError as e:
                ditolak.append((no, baris, str(e)))
    return valid, ditolak

def hitung_alasan(ditolak):
    jumlah = {}
    for no, isi, alasan in ditolak:
        jumlah[alasan] = jumlah.get(alasan, 0) + 1
    return jumlah

# Eksekusi pengujian untuk Lembar Kerja Butir 6
if __name__ == "__main__":
    valid, ditolak = baca_log("log_mikrofon.csv")
    print("=== HASIL VALIDASI LOG MIKROFON ===")
    print(f"Jumlah Data Valid   : {len(valid)}")
    print(f"Jumlah Data Ditolak : {len(ditolak)}")
    print("\nRincian Alasan Penolakan (hitung_alasan):")
    print(hitung_alasan(ditolak))
    
    print("\nDaftar Baris yang Ditolak:")
    for no, isi, alasan in ditolak:
        print(f" Baris {no:2d} | {isi:12s} | Alasan: {alasan}")