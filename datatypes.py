#Выводит тип переменной
a=15.5
print(type(a))
b=6
print(type(b))
c=16.78
print(type(c))

#изменение типа данных
a=int(a)
print("a=", a)

a = 10
print("Десять " + str(a))

a = 'я изучаю Python' 
print(list(a))

a = 'привет'
print(set(a))

a = ('red', 'blue', 'green')
print(list(a))

name = input('Как тебя зовут? ')
print(f'Привет, {name}!')
age = int(input('Сколько тебе лет? '))
print(f'Здорово! В следующем году тебе будет {age + 1}!')
