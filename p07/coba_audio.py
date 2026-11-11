
import numpy as np
from audio import hitung_dbfs, ke_level_db

daftar_uji = [
    ("konstan 0.1", np.full(100, 0.1)),
    ("konstan 0.01", np.full(100, 0.01)),
    ("konstan 0.001", np.full(100, 0.001)),
    ("konstan 0.5", np.full(100, 0.5)),
    ("nol", np.zeros(100)),
    ("sinus 0.1", 0.1 * np.sin(2 * np.pi * np.arange(16000) / 160))
]

for nama, sinyal in daftar_uji:
    try:
        print(nama)
        print("Hasil dBFS:", round(hitung_dbfs(sinyal), 2))
        print("Level suara:", round(ke_level_db(sinyal), 2), "dB")
    except ValueError as e:
        print("Error:", e)
