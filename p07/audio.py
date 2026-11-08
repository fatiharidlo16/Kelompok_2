import numpy as np
import sounddevice as sd

LAJU_CUPLIK = 16000
OFFSET_DB = 100.0

def daftar_masukan():
    perangkat = sd.query_devices()
    for i, p in enumerate(perangkat):
        if p["max_input_channels"] > 0:
            print(i, p["name"])

def rekam(durasi=2):
    data = sd.rec(
        int(durasi * LAJU_CUPLIK),
        samplerate=LAJU_CUPLIK,
        channels=1,
        device=2
    )
    sd.wait()
    return data[:, 0]

def ke_level_db(sinyal):
    dbfs = hitung_dbfs(sinyal)
    return dbfs + OFFSET_DB

def hitung_dbfs(sinyal):
    rms = float(np.sqrt(np.mean(np.square(sinyal))))

    if rms == 0:
        raise ValueError("sinyal kosong, RMS sama dengan 0")

    return 20 * np.log10(rms)