from gpiozero import AngularServo
from perangkat import Sensor, Aktuator
from statistik import rata_rata, tertinggi
from validasi import dalam_rentang, BATAS_BAWAH, BATAS_ATAS


class Mikrofon(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "dB")

    def proses(self):
        return rata_rata(self.data)


class SensorSuhu(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "C")

    def proses(self):
        return tertinggi(self.data)


class Servo(Aktuator):
    def __init__(self, nama, nilai_awal=0, pin=None):
        super().__init__(nama, nilai_awal)
        self.servo = None

        if pin is not None:
            self.servo = AngularServo(
                pin,
                min_angle=0,
                max_angle=180
            )
            self.servo.angle = nilai_awal

    def gerak_ke(self, sudut):
        if not dalam_rentang(sudut, 0, 180):
            return False

        self.nilai = sudut

        if self.servo is not None:
            self.servo.angle = sudut

        return True

    def lebar_pulsa(self):
        if self.servo is None:
            return 0

        return self.servo.pulse_width * 1000

    def proses(self):
        return self.nilai
    
class LampuIndikator(Aktuator):
    def atur(self, persen):
        if persen < 0:
            persen = 0

        if persen > 100:
            persen = 100

        self.nilai = persen / 100

    def proses(self):
        return self.nilai