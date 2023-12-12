#Напишите программу, печатающую числа от 1 до 100. Вместо чисел кратных трём, программа должна печатать 'Fizz'. Вместо чисел кратных пяти - 'Buzz'. Если число кратно и трём, и пяти, программа должна печатать 'FizzBuzz'.
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
            print('Fizz')
    elif i%5==0:
            print('Buzz')
    else:
        print(i)
#Укладываем стандартное решение в стандартный однострочник
print('\n'.join('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else str(i) for i in range(1, 101)))
#Избавляемся от Join, приручаем Print
[print('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i) for i in range(1, 101)]
#Добавляем срез, укрощаем if else
[print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) for i in range(1, 101)]
#Оптимизируем срез, избавляемся от if else
[print('FizzBuzz'[i * i % 3 * 4:8 - -i ** 4 % 5] or i) for i in range(1, 101)]
#Заменяем срез конкатенацией, вертаем оператор modulo
[print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i) for i in range(1, 101)]
#Оптимизируем решение. Выравниваем по длине со срезом
[print((i%3<1)*'Fizz'+(i%5<1)*'Buzz' or i) for i in range(1, 101)]
#Уходим в отрыв. Модифицируем окончательный вариант
[print(i%3//2*'Fizz'+i%5//4*'Buzz' or i+1) for i in range(100)]
