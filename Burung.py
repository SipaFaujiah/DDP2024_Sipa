from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
    def info_Burung(self):
        super().info_Animal(),
        print("Paruh \t\t\t : ", self.paruh, "\nWarna Bulu \t\t: ", self.warna_bulu)
        
burung_beo = Burung("Beo", "Jagung", "Darat", "Bertelur", "Melengkung", "Warna warni")
burung_beo.info_Burung()
print("===================================")
burung_merpati = Burung("Merpati", "Beras", "Darat", "Bertelur", "Lurus", "Putih")
burung_merpati.info_Burung()
print("===================================")