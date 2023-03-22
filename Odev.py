#Homework1 :

# Python Veri Tipleri

# int : Tam sayıları ifade eder. - sonsuzdan + sonsuz kadar kapsar.  
sayi = 2
print(sayi)
print(type(sayi))

# float : Ondalık sayıları ifade eder.
sayi1 = 0.5
print(sayi1)
print(type(sayi1))

# complex : Karışık sayıları ifade eder.
a = 2j
print(a)
print(type(a))

# str : Metinsel türünü ifade eder.
baslik = "Veri Tipleri"
print(baslik )
print(type(baslik))

# bool : True-False sonuç döndürür.
p = 5
s = 55
print(p>s)
# list : Listeleme yapar.
x = ["Samsun","İstanbul","Edirne"]
print(x)
print(type(x))

# tuple : () ile tanımlanan listeleme veri türüdür.
b = ("C#","Python","Java")
print(b[0],b[1],b[2])
print(type(b)) 

# dict : Haritalama veri türlerini ifade eder.
c = {"name" : "Yaser","Age" : 24}
print(c)
print(type(c))

# set : Kümedir,listeden farkı ise ; liste birden fazla kez tekrar eden elemanlar içerebilir, sıralıdır ve değiştirilebilirken, küme benzersiz elemanlar içerir, sırasızdır ve değiştirilebilir.


#Boş veri : None

#Homework2
#kodlama.io daki değerlendirme-ödev1-ödev2-kursların her birinin ismi string veri türüne örnektir.
#kodlama.io daki kursları tamamlama oranları ise int örnektir.
#kodlama.io daki tüm kurslar-eğitmenler list'e örnektir.


#Homework3
#kodlama.io daki kursların ders videolarını izleyebilmek için programa dahil ol butonunu onaylamamız lazım bu da br şart bloğudur.

programaDahilOl = True
if programaDahilOl ==True:
    print("Ders videolarina erişiminiz sağlanmiştir.")
else:
    print("Programa dahil olmadan kursun içeriğine erişim sağlayamazsiniz.")
