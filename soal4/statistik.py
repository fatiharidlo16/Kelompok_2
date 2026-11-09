def rentang(data):
    """Mengembalikan tuple (nilai terkecil, nilai terbesar)."""
    if not data:
        return (None, None)
    return (min(data), max(data))

def ringkasan(data):
    """Mengembalikan dictionary berkunci jumlah, min, maks, dan rata."""
    if not data:
        return {"jumlah": 0, "min": None, "maks": None, "rata": 0}
    return {
        "jumlah": len(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data)
    }

if __name__ == "__main__":
    data_uji = [12.0, 15.0, 15.0]
    
    r_rentang = rentang(data_uji)
    r_ringkasan = ringkasan(data_uji)
    
    print("Rentang:", r_rentang)
    print("Ringkasan:", r_ringkasan)
    print("Nilai rata:", r_ringkasan["rata"])