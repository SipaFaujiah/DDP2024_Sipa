from Person import *

class Mahasiswa(Person):
    prodi=""
    semester=0
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama,gender,umur)
        self.prodi = prodi
        self.semester = semester
    def Cetak(self):
        super().Cetak()
        print("Prodi \t\t : ", self.prodi, "\nSemester \t : ", self.semester)
        print("===========================")
        
Sri = Mahasiswa("Sri", "Wanita", 20, "Teknik Informatika", 3)
Sri.Cetak()

Siti = Mahasiswa("Siti", "Wanita", 21, "Sistem Informasi", 5)
Siti.Cetak()
