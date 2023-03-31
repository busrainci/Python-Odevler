# sınıflar => class
# modules
# paket yönetimi 

class Human: #(Human = insan)  erguman = parametre
    name = "Halit"
    def __init__(self,name):   #init = initialize 
        self.name = name
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):  #self = kendisi demek paramtereye ilk bu yazılmalıdır 
        print(f"{self.name} {sentence}")
    def walk(self):
        print("Human is walking...")
    
#instance => örnek nesnelere erişilmesi için nesnelere birer örnek vererek erişilebilir :
human1 = Human("Yaser")  # newlwmiş olduk yani üstteki kalıbı örnekledik.
human1.talk("merhaba")
human1.walk()
print(human1)

human2 = Human("Büşra")
human2.talk("Selam")
human2.walk()
print(human2)

