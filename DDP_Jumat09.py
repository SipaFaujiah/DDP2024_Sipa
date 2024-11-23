#No 1
#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0)) 
# # Output: 32.0
#print(celcius_ke_fahrenheit(100))
# # Output: 212.0

def celcius_ke_fahrenheit(cecius):
    print()
    hasil_koversi =(cecius * 9/5) + 32
    return hasil_koversi

celcius1 = 0
print(f"hasilnya adalah {celcius_ke_fahrenheit(celcius1)}")
print(celcius_ke_fahrenheit(100))


#No2
#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))
# # Output: True
#print(is_genap(7)) 
# # Output: False
print("========================================")

def is_genap(angka):
    print()
    hasil = angka % 2 == 0
    return hasil
print(is_genap(4))
print(is_genap(7))

#No3
#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus :
#nilai (80) #lulus
#nilai(60) #gagal
print("========================================")

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return "lulus"
    else :
        return "gagal"
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))


# outputnya samil bisa pulang kalo gagal ga pulang
# ini tantangan kalo bisa pulng I
print("========================================")
def ddp(ketentuan):
    print()
    if ketentuan == "bisa":
        print("Syamil pulang")
    elif ketentuan == "gagal":
        print("Syamil ga pulang")
    else:
        print("inputan tidak valid")
ddp("bisa")


#No4
#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19
print("========================================")
def bilangan_ganjil(angka):
    print()
    for i in range(1, angka, 2):
        print(i, end="")
bilangan_ganjil(20)
