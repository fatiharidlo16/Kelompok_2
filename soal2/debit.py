def hitung_rata_rata(data):
    """Menghitung rata-rata dari list data debit."""
    if not data:
        return 0
    return sum(data) / len(data)

def cari_terendah(data):
    """Mencari nilai terkecil dari list data debit."""
    if not data:
        return None
    min_val = data[0]
    for nilai in data:
        if nilai < min_val:
            min_val = nilai
    return min_val

def cek_status(nilai):
    """Mengecek kategori status berdasarkan nilai debit air."""
    if nilai < 10.0:
        return "Rendah"
    elif 10.0 <= nilai <= 20.0:
        return "Normal"
    else:
        return "Tinggi"