n=int(input("Введите число: "))
if n<10:
    print("число меньше 10")
else:
    print("число больше 10")

r=int(input("Vvedite radius: "))
if r>=0:
    print("Dlina okrujnosti: ", 2*3.14*r)
    print("ploshad= ", 3.14*r**2)
else:
    print("Try again")

password=input("password: ")
if password=="moon":
    print("Wellcome!")
else:
    print("Access is denied!")
