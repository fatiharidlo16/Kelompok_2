import pin_tiruan
from komponen import Servo

servo = Servo("servo-uji", pin=18)

print("Posisi awal:", servo.proses())

for sudut in [-0.1, 180.1, 200, float("nan")]:
    servo.gerak_ke(sudut)
    print(
        "sudut", sudut,
        "| posisi", servo.proses(),
        "| lebar pulsa", round(servo.lebar_pulsa(), 3), "ms"
    )

print("\nPengujian penolakan sudut:")

for sudut in [-0.1, 180.1, 200]:
    hasil = servo.gerak_ke(sudut)
    print(
        "sudut", sudut,
        "| diterima", hasil,
        "| posisi", servo.proses(),
        "| lebar pulsa", round(servo.lebar_pulsa(), 3), "ms"
    )