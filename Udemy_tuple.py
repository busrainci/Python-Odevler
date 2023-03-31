# tupleListe = (2,4,6,"Ankara",(2,3,4),[])
# liste = [2,4,6,"Ankara",[3,4,5],()]

# liste[0] = "6"
# print(type(liste[0]))

# #  tupleListe[0] = 6    =>   # tuple da oluşturulan hiçbir eleman değiştirilemez. tuplenın bellekte yer tutuşu daha azdır sadece okunabilir oldukları için

# tupleDeger= ("Yaser")
# print(tupleDeger)
# print(type(tupleDeger))


# print(tupleListe[1:2])
# print(liste[1:2])


# print(tupleListe[-2])
# print(liste[-2])



# print(type(tupleListe))
# print(type(liste))
# print(tupleListe)
# print(liste)
# print(len(tupleListe))
# print(len(liste))


# studentsSet ={"Yaser","Büşra","Ulutürk","Yiğit"}  #listede var olan data değiştirilmez fakat yeni bir data eklenebilir.

# print(studentsSet)

# for student in studentsSet:
#     print(student)

# print("Derin" in studentsSet)
# print("Yaser" in studentsSet)

# if "Yaser" in studentsSet:
#     print("Listede var")

# studentsSet.add("İnci")
# print(studentsSet)

# studentsSet.update(["dilay","mehmet","malika","enes"])
# print(studentsSet)

# print(len(studentsSet))

# studentsSet.remove("İnci")
# print(studentsSet)

# studentsSet.discard("İnci")   # discard : silinen elemanın tekrar silinmesi durumunda hata vermeyip atlamasını sağlar
# print(studentsSet)

# print(len(studentsSet))

# x = studentsSet.pop()
# print(studentsSet)

# x = studentsSet.clear()
# print(len(studentsSet))
# del studentsSet
# print(studentsSet)

# print("**************************   SET  UNİON    *******************************")

# setA = {1,2,3,4,5}
# setB = {1,3,4,6,7,8}

# print(setA | setB)  # iki kümeyi birleştirip aynı elemanları tekrarlamadan yazar.
# print(setA.union(setB))
# print(setB.union(setA))

# print(setA & setB)   # iki kümedeki ortak elemanları yazar yani kesişim kümesidir.
# print(setA.intersection(setB))
# print(setB.intersection(setA))

# print(setA - setB)  # iki kümenin birbirinden ayrı olan kısımlarını ifade eder yani iki küme farkıdır.
# print(setA.difference(setB))
# print(setB.difference(setA))

# print(setA ^ setB)  # iki kümenin ortak olmayan elemanlarını ifade eder.
# print(setA.symmetric_difference(setB))
# print(setB.symmetric_difference(setA))

# print("*******************************  DİCTİONARY  *******************************************")

# sozluk = {
#             "book" : "kitap",
#             "table" : "masa"
#          }


# sozluk2 = dict(kitap = "book", masa = "table")
# sozluk["book"] = "kitap1"
# sozluk["pencil"] = "kalem"
# del(sozluk["book"])
# print(sozluk)
# print(sozluk2)
# print(len(sozluk2))

# print("**************   IF ELSE  ******************")


# sayi1 = 20
# sayi2 = 20


# if sayi1<=sayi2:
#     print("Birşey")
#     print("Birşey daha")
# print("başka birşey ")


# lights = ["red","yellow","green"]

# currentLight = lights[1]
# print(currentLight)


# if currentLight == "red":
#     print("STOP!")
# elif currentLight =="yellow":
#     print("READY!")
# else :
#     print("GO!")

# sayi = int (input("sayı giriniz : "))

# if sayi > 0:
#     print("pozitif sayıdır.")
# elif sayi < 0 :
#     print("negatif sayıdır.")    
# else:
#   print("Nötr sayıdır.")

# sayi1= int(input("birinci sayıyı giriniz : "))
# sayi2 = int(input("ikinci sayıyı giriniz : "))
# sayi3 = int(input("üçüncü sayıyı giriniz : "))

# if (sayi1 > sayi2) and (sayi1 > sayi3):
#     print(f"En büyük sayı : {sayi1}")
# elif (sayi2 < sayi1) and (sayi2 > sayi3):
#     print(f"ortaca sayı : {sayi2}")
# else :
#     print(f"en küçük sayı : {sayi3}")


print("*********************  FOR DÖNGÜSÜ  *************************")


# sehirler = ["Ankara", "İstanbul", "İzmir"]
# # print(sehirler[0])
# # print(sehirler[1])
# # print(sehirler[2])

# for sehir in sehirler:
#     if sehir == "İzmir":
#         continue
#     print(sehir + " için kod : " + sehir[0:3])
#     print("***************")


# for x  in range(1,11,3):
#     print(x)

# continue ile break arasındaki fark şudur : break döngüde istediğini bulunca döngüyü tamamen sonlandırır.İstanbulu bulduktan sonra altındaki printleri ve sıradaki şehirleri çalıştırmaz.
# continue ise döngüde istediğini bulunca şart bloğunun dışındakini çalıştırmayıp pas geçer fakat döngü sıradan gezmeye devam eder. İstanbulu bulduktan sonra altındaki 
# printleri çalıştırmaz fakat izmirden döngüyü gezmeye devam eder.

# print("********************   WHİLE DÖNGÜSÜ  **************************")

# sayac = 1
# sonuc = 0


# while sayac <= 10:
#     sonuc = sonuc + sayac
#     sayac = sayac + 1 

# print(sonuc)


# sayi =int(input("Kaç yıldız olsun : "))

# yildiz =""

# for x in range(1,sayi+1):
#     yildiz = yildiz + "*"
#     print(yildiz)

# sayi = int(input("sayı giriniz : "))
# asalMi = "evet"

# for x in range(2,sayi):
#     if (sayi % x) == 0:
#         asalMi = "hayır"
#         break
   
# if asalMi == "evet":
#     print("ASAL")
# else:
#     print("ASAL DEĞİL")

print("***************  FONKSİYONLAR  ******************")

# def selamVer(isim = "ziyaretçi "):
#     print(isim + "Merhaba :)")

# selamVer("Büşra ")
# selamVer("Yaser ")
# selamVer()

# def selamVer2(isim = "ziyaretçi", soyIsim = " arkadaş "):
#     print("Merhaba "+ isim + soyIsim)

# selamVer2("Büşra")
# selamVer2("Yaser ","Ulutürk ")

# def dikUcgenAlaniHesapla(a,b):
#     return a*b/2

# alan = dikUcgenAlaniHesapla(2,3)
# print(alan)

# # lambda ile çalıştırmak : 

# dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

# print(dikUcgenAlaniHesapla2(3,6))

# print(type(dikUcgenAlaniHesapla2))

# property = özellik demektir.

# class Person : 
#     def __init__(self,firstName,lastName,age):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age

# person1 = Person("Yaser","ULUTÜRK",24)
# print(person1.firstName,person1.lastName,person1.age)

# class Worker:
#     def __init__(self,salary):
#         self.salary = salary
# class Customer(Person):
#     def __init__(self,creditCardNumber):
#         self.creditCardNumber = creditCardNumber

# ahmet = Worker()
# mehmet = Customer()

def topla(sayi1, sayi2):
    print("Toplam : "+ str((sayi1 + sayi2)))
def carp(sayi1, sayi2):
    print("Çarp : "+ str((sayi1 * sayi2)))