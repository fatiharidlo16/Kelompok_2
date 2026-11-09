from komponen import LampuIndikator

if __name__ == "__main__":
    lampu = LampuIndikator("led-1")
    lampu.nyalakan()  # Nyalakan agar lampu aktif

    lampu.atur(80)
    print("atur(80):", lampu.proses())

    lampu.atur(150)
    print("atur(150):", lampu.proses())

    lampu.atur(-5)
    print("atur(-5):", lampu.proses())