# faiz = 1.59
# vade = "36"
# krediAdi= "İhtiyaç Kredisi"

# print(type(faiz))
# print(type(vade))
# print(type(krediAdi))


# print(int(vade)+12)
# faiz = str(faiz)
# print(type(faiz))
# # yorum satırı yapmak için istenilen satıra imleç olduğunda ctrl+ö ,yorum satırından çıkartmak için de öyle yapmak gerekir.

# vade = int#(input("Lütfen istediğiniz vade sayısını giriniz : "))  # bu satırdanitibaren vade int typedir.
# print(type(vade))
# print(vade+ 12)

# # string interpolation
# # seçtiğiniz vade sonucu ortaya çıkan vade : 
# print("seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
# print("seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi =10) )
# print(f"seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")


# isim=  "halit"  #input("isminizi giriniz : ")
# metin = "Merhaba {name}".format(name=isim)
# print(metin)

# # f-string
# metin = f"hoşgeldiniz {1+1}"
# print(metin)


# dizi = ["ihtiyaç kredisi",5.2,10,True]
# print(dizi)

krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
print(type(krediler))

print(krediler[0])
#print(len()) #length


krediler.append("özel kredi")
print(krediler)

krediler.append("X kredi")
print(krediler)

krediler.pop(1)
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)

krediler.remove("taşıt kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z Kredisi"])
print(krediler)

# for döngüsü  i=0 i<10 i++


for i in range(10):
    print("**")
    print(i)
print("***********")

for i in range (5,11):
    print(i)

print("*************")
for i in range (0,51,10):
    print(i)
print("***************")


krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
for kredi in krediler:
    print(kredi)
print("**********")
for i in range(len(krediler)):
    print(krediler[i])

print("***************")

i = 0
while i<10:
    print("x")
    i += 1
print("y")
print("*********")

while True:
    print("X")
    break
print("*********")

i = 0
while i< len(krediler):
    if krediler[i] == "konut kredisi":
        break
    print(krediler[i])
    i +=1

#fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():  #fonksiyon tanımladık ve bunu ne kadar nerede çağırırsak orada o kadar tekrarlar.
    print(100-20)

calculate()
calculate()

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)