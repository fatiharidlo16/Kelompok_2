
def baca_mentah(nama_berkas):
    data = []

    with open(nama_berkas, "r") as berkas:
        next(berkas)  # Lewati baris header

        for baris in berkas:
            kolom = baris.strip().split(",")

            try:
                nilai = float(kolom[1])
                data.append(nilai)
            except (ValueError, IndexError):
                continue

    return data
