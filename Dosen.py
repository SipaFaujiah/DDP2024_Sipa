from Person import *


class Dosen(Person):
    gelar =""
    jabatan =""
    gaji = 0
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    def setGaji(self, uang):
        self.gaji += uang
    def Cetak(self):
        super().Cetak()
        print("Gelar \t\t :", self.gelar, "\nJabatan \t :", self.jabatan, "\nGaji \t\t :", self.gaji)
        print("=========================")
Budi = Dosen("Budi", "pria", 35, "S.kom", "Dosen")
Budi.setGaji(5000000)
Budi.Cetak()

Asep = Dosen("Asep", "Pria", 44, "S.Sos", "Dosen")
Asep.Cetak()