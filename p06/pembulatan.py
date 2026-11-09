from baca_log import baca_log
from statistik import rata_rata
from galat import galat_relatif, status

valid, _ = baca_log("log_mikrofon.csv")
rata = rata_rata(valid)
acuan = 62.4412

for i in range(4):
    r_rata = round(rata, i)
    g = galat_relatif(r_rata, acuan)
    st = status(g)
    print(f"round(rata, {i}) = {r_rata} | Galat: {g:.4f}% | Status: {st}")