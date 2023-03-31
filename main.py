print("Kodlama.io") 
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "İhtiyaç kredisi"
print(baslik)
#int => tam sayı ifadesi
vade = 36
ekVade=6
vade2 = "36"

#float,decimal,double
aylikOdeme = 200.50

#bool,#boolean => true-false
yukselisteMi = True

#matematiksel operatörler
print(5 + 5)
print(vade+12)
print(ekVade+vade)
print(36+6)

#------------
print("------------")
print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

#*
print("************")
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)

#/
print("///////////")
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade/2
fiyat = 100
indirimliFiyat= fiyat-20

print(yeniVade)
print(indirimliFiyat)

#% => mod operatör
print("%%%%%%")
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

#mantıksal operatorler
print("+++++++++++")
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)

print(1 >= 1)
print(3 <= 1)

print(1 < 2)
print(1 < 1)
print(1 < 10)

print(1 != 1)
print(1 != 2)

# or and
print("&&&&&&&&&&&")
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)
print(2 > 1 or 1 > 2 and 3 > 2)




# karar yapıları
#if else
sayi1 = 15
sayi2 = 15
# sayi1>sayi2 ise ekrana sayi1 daha büyüktür yaz

if sayi1<sayi2:
    print("sayi2 sayi1'den daha büyüktür.")
elif sayi1 == sayi2 : 
    print("iki sayı eşittir.")
else:
    print("sayi1 sayi2'den  daha büyüktür.")
    print("sayfayı kapatabilirsinizz..")

print("Burası if bloğunun dışıdır.")