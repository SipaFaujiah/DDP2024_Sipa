class Gempa :
    lokasi = ''
    skala = ''
    
    #contractor
    def __init__(self,lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
        #method / fungsi
    def dampak(self):
        if self.skala <2 :
            ket = 'Gempa tidak berasa'
        elif self.skala >2 and self.skala <4 :
            ket = ' Bangunan Retak - Retak'
        elif self.skala >4 and  self.skala <6 :
            ket = 'Bangunan Roboh'
        else :
            ket = 'Bangunan roboh dan berpotensi tsunami'
        print('Lokasi Gempa', self.lokasi, 'skala gempa', self.skala, 'Dampak Gempa', self.dampak, ket)