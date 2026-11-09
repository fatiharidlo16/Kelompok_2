class Perangkat:
    def __init__(self, nama):
        self.nama = nama
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

    def proses(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan metode ini.")

class SensorSuhu(Perangkat):
    # Tanpa constructor sendiri, mewarisi __init__ dari Perangkat
    def proses(self):
        if not self.data:
            return 0
        return max(self.data)

class SensorDebit(Perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)