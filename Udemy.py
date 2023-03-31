x = 10 #integer
y = "10" #string
isim = "Engin"
soyisim = "Demiroğ"
telNo = "51626486255"


print(type(x))
print(type(y))
print(x+10)
print(int(y)+15) #tip değişikliği yapıldı.

mesaj = "merhaba dünya"
print(mesaj[2])
print(mesaj[2:5])
yeniMesaj = mesaj[:2]
yeniMesaj = mesaj[12:13]
print(yeniMesaj)
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

# # lower upper
print(mesaj.upper())
print(mesaj.lower())

# # replace
print(mesaj.replace("ü","u"))
print(mesaj)
print(mesaj.replace("a","e"))

# # split ve strip
bilgi = "Engin;Demiroğ;33;Ankara".strip()
# print(bilgi.split())
# print(bilgi.split(";"))
print("Adı = " + bilgi.strip(";")[0:5])

# # input
ad = input("Adınız = ")
sayi1 =int(input("sayı1 ="))
sayi2 = int(input("sayı2 ="))
print(sayi1+sayi2)

# # Listeler
ogrenciler = ["Yaser","Büşra","Yiğit"]
print(ogrenciler[0])
ogrenciler.append("Ulutürk")
print(ogrenciler)
ogrenciler.remove("Yiğit")
print(ogrenciler)
ogrenciler[1]="Yiğit"
print(ogrenciler)

# # Liste constructor

sehirler = list(("Samsun","İstanbul","Edirne","Edirne"))
print(sehirler)
print(len(sehirler))

# Diğer Fonksiyonlar
# print(sehirler.clear())
print("Edirne sayısı : " + str(sehirler.count("Edirne")))
print("Samsun indexi : " + str(sehirler.index("Samsun")))
sehirler.pop(1)
sehirler.insert(0,"İstanbul")
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0] = "İzmir"


print(sehirler)
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print(sehirler)


import Udemy_tuple

Udemy_tuple.topla(1,6)
Udemy_tuple.carp(4,8)