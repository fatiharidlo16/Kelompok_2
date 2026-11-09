import csv

def baca_log(nama_file):
    data_valid = []
    data_ditolak = []
    
    with open(nama_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # Lewati baris header (Baris 1)
        
        for nomor_baris, row in enumerate(reader, start=2):
            # 1. Jumlah kolom harus dua
            if len(row) != 2:
                data_ditolak.append((nomor_baris, row, "Jumlah kolom bukan dua"))
                continue
                
            waktu, val_str = row[0].strip(), row[1].strip()
            
            # 2. Nilai debit harus berupa angka
            try:
                debit = float(val_str)
            except ValueError:
                data_ditolak.append((nomor_baris, row, "Nilai debit bukan angka"))
                continue
                
            # 3. Nilai harus berada pada rentang 5 sampai 25 (inklusif)
            if not (5.0 <= debit <= 25.0):
                data_ditolak.append((nomor_baris, row, f"Nilai {debit} di luar rentang 5-25"))
                continue
                
            data_valid.append((waktu, debit))
            
    return data_valid, data_ditolak

def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)

def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh 0.")
    return (abs(hasil - acuan) / acuan) * 100

if __name__ == "__main__":
    file_path = "log_debit.csv"
    valid, ditolak = baca_log(file_path)
    
    print(f"Jumlah data valid: {len(valid)}")
    print(f"Jumlah data ditolak: {len(ditolak)}")
    
    if valid:
        total_debit = sum(nilai for waktu, nilai in valid)
        rata_rata = total_debit / len(valid)
        print(f"Rata-rata data valid (2 desimal): {rata_rata:.2f}")
        print(f"Rata-rata presisi penuh: {rata_rata}")
        
        # Pengujian Galat (Bagian C)
        acuan = 13.5714
        g_abs = galat_absolut(rata_rata, acuan)
        g_rel = galat_relatif(rata_rata, acuan)
        
        print(f"Galat Absolut: {g_abs:.4f}")
        print(f"Galat Relatif (%): {g_rel:.4f}%")
        
        if g_rel <= 0.5:
            print("Status: LULUS")
        else:
            print("Status: TIDAK LULUS")