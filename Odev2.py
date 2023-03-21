# Homework2

print("----------------Öğrenci Kayıt Sistemine hoşgeldiniz----------------")

loop = True
students = ["Yaser ULUTÜRK","Büşra İNCİ","Dilay ÇAKMAK","Mehmet DAĞ"]

def menu():
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1 - Öğrenci Ekle\n"
                "2 - Öğrenci Sil\n"
                "3 - Öğrencileri Listele\n"
                "4 - Öğrenci Numarası Öğrenme\n")
                
    if sec == "1":
        print("Kayıt ekleme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        addStudent()
    if sec == "2":
        print("Kayıt Silme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        removeStudent()
    if sec == "3":
        print("Öğrenciler listeleniyor...")
        print("-----------------------------------------------------------")
        studentsList()
    if sec == "4":
        print("Öğrenci Numarası öğrenme sayfasına gidiliyor...")
        print("-----------------------------------------------------------")
        studentNum()
 
# öğrenci kayıt
def addStudent():
    print(students)
    add = input("Eklemek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    students.append(add)
    print(students)
    print("Öğrenci kaydı oluşturulmuştur.")
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            addStudent()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

# öğenci silme
def removeStudent():
    print(students)
    remove = input("Silmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    if remove in students:
        students.remove(remove)
        print("Öğrenci kaydı silinmiştir.")
    else:
        print("-----------------------------------------------------------")
        print("hatalı giriş yaptınız veri bulunamadı tekrar deneyin")
   
        removeStudent()
    print(students)
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            removeStudent()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

def studentsList():
    print(students)
    return menu()

def studentNum():
    print(students)
    num = input("Numrasını öğrenmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    stunum = students.index(num)
    print("{} Öğrencinin numarası: {} ".format(num,stunum))
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            studentNum()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

while loop:
    menu()