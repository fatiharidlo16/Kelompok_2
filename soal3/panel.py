from lampu import Lampu

class PanelLampu:
    def __init__(self):
        # Komposisi: PanelLampu memiliki dua objek Lampu sebagai atributnya
        self.lampu_merah = Lampu("merah")
        self.lampu_hijau = Lampu("hijau")

    def nyalakan_semua(self):
        self.lampu_merah.nyalakan()
        self.lampu_hijau.nyalakan()

    def tampilkan(self):
        print(self.lampu_merah)
        print(self.lampu_hijau)

# Pengujian sesuai instruksi soal
if __name__ == "__main__":
    # Buat satu panel
    panel = PanelLampu()
    
    # Nyalakan semua lampu
    panel.nyalakan_semua()
    
    # Atur lampu_hijau menjadi 30
    panel.lampu_hijau.atur(30)
    
    # Tampilkan kondisi panel
    panel.tampilkan()