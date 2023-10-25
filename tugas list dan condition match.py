print('nomer 1')
kendaraan = ['vario', 'motor', 150, 'merah', 2]
print(kendaraan)
kendaraan.append(20000000)
kendaraan.append('matic')
print(kendaraan)
kendaraan.insert(2,'Honda')
print(kendaraan)
print('')

print('nomer 2')
print('angka 1 untuk hitung  persegi')
print('angka 2 untuk hitung  lingkaran')
print('angka 3 untuk hitung  segitiga')
raihan = input('mau hitung apa nih?')

match raihan :
  case '1' :
    sisi = int(input('masukkan sisi :'))
    persegi = sisi * sisi
    print('hasil luas persegi :', persegi)
  case '2' :
    v = 22/7
    r = int(input('masukkan jari2 :'))
    luas = v *r*r
    print('hasil luas lingkaran :', luas)
  case '3' :
    a = int(input('masukkan alas :'))
    t = int(input('masukkan tinggi :'))
    luassegi = a*t/2
    print('hasil luas segitiga :', luassegi)
  case _:
    print('masukkan sesuai yang di perintah')
print('')

print('latihan aritmatika')
angka = int(input('masukkan sebuah angka : '))
if angka % 2 == 0 :
  print('angka',angka,'termasuk bilangan genap')
else :
  print('angka',angka,'termasuk bilangan ganjil')