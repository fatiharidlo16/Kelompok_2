
TOLERANSI = 0.5


def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("acuan 0, galat relatif tidak dapat dihitung")

    return galat_absolut(hasil, acuan) / abs(acuan) * 100


def status(hasil, acuan):
    if galat_relatif(hasil, acuan) <= TOLERANSI:
        return "LULUS"
    return "TIDAK LULUS"
