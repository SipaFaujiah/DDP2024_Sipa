from Animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, corak_sisik, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.corak_sisik = corak_sisik
        self.berbisa = berbisa
    def info_Ular(self):
        super().info_Animal()
        print("Corak Sisik \t\t :",self.corak_sisik,"\nBerbisa \t\t :",self.berbisa)
        
ular_piton = Ular("Ular sawah","Tikus / hewan kecil","Sawah","Bertelur","Berbutir","Tidak berbisa",)
ular_piton.info_Ular()
print("==================================================")
ular_cobra = Ular("Cobra","daging / tikus","Rawa - Rawa","Bertelur","Hitam","berbisa")
ular_cobra.info_Ular()
print("======================================================")