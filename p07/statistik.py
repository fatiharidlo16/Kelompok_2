def rata_rata(data):
    return sum(data) / len(data)

def tertinggi(data):
    return max(data)

def terendah(data):
    return min(data)

def rentang(data):
    return (min(data), max(data))

def median(data):
    data_terurut = sorted(data)
    n = len(data_terurut)
    if n == 0:
        return 0
    tengah = n // 2
    if n % 2 == 1:
        return data_terurut[tengah]
    else:
        return (data_terurut[tengah - 1] + data_terurut[tengah]) / 2

def ringkasan(data):
    return {
        "jumlah": len(data),
        "rata": round(rata_rata(data), 2),
        "min": min(data),
        "maks": max(data),
        "median": median(data),
    }