from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, bisa_konsumsi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.bisa_konsumsi = bisa_konsumsi
    def info_Ikan(self):
        super().info_Animal()
        print("Habitat \t\t :",self.habitat, "\nBisa dikonsumsi \t :",self.bisa_konsumsi)
        
        
ikan_nila = Ikan("Nila","Pelet Ikan","Air","Bertelur","Tawar","Bisa")
ikan_nila.info_Ikan()
print('===============================================')
ikan_hiu = Ikan("Hiu","Ikan Kecil/Cumi","Air","Beranak","Air Laut","Tidak")
ikan_hiu.info_Ikan()
print('===============================================')