# değişkenlerin yerlerini değiştirmek

x = 10
y = 20

print("x = "+ str(x))
print("y = "+ str(y))

# 1.yol
temp = x
x = y
y = temp

# 2.yol
x,y = y,x
print(x)
print(y)


# 420km = x mil

donusumOrani = 0.621371192
km = int(input("kaç km = "))

mil = km*donusumOrani
print(str(km) + "Km = "+ str(mil) + " mil eder.")

