#1
kendaraan = ['beat karbu', 'motor', '200', 'pink', 3]
print(kendaraan)

kendaraan.append('10jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)


#2
angka_pilihan = int(input("""Masukkan Pilihan:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga"""))
match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukkan nilai sisi:"))
        luas_persegi = sisi** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2 ")
    case 2:
        print("Menghitung Luas Lingkaran")
        jari_jari = float(input("Masukkan jari-jari lingkaran:"))
        luas_lingkaran = 3.14* jari_jari ** 2
        print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran}")
    case 3:
        print("Menghitung Luas Segitiga")
        alas = float(input("Masukkan panjang alas segitiga:"))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = alas*tinggi /2
        print("Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga:.2f}")
    case _:
        print("salah pilih")
        
#
biodata_diri =int(input(""" Masukkan pilihan:
1. Nama
2. Nim
3. Rombel"""))
match biodata_diri:
    case "Nama":
        print("Sipa Faujiah")
        
    case "Nim":
        print("0110124111")
    case "Rombel":
        ("SI07")
    case _:
        print("tidak terinput")
        
        