my_array = ( [1,2,3,4,5])
print(my_array[1])
print(my_array[2])
print(my_array[0])

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)


arr=[[5, 7, 6], [0, 1, 3], [5, 8, 9]]
print(arr[1][2])
print(arr[0][1])
print(arr[1][2])

my_list = [2, 4, 6, 8, 10]
if 7 in my_list:
     print("Число 7 найдено в массиве")
else:
     print("Число 7 не найдено в массиве")

#Добавляет элемент на определенную позицию
my_array = [1, 2, 3, 4, 5]
my_array.insert(0, 7)
print(my_array)

#Добавляет 7 в самый конец массива
my_array = [1, 2, 3, 4, 5]
my_array.append(7)
print(my_array) # [1, 2, 3, 4, 5, 7]

#созздание нового массива, с добавлением нового элемента
my_array = [1, 2, 3, 4, 5]
new_array = my_array + [7]
print(new_array) # [1, 2, 3, 4, 5, 7]

#Добавление элемента на определенную позицию
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10
print(my_list) # [10, 2, 3, 4, 5]

#Удаление элемента вм ассиве
arr = [8, 5, 6, 1]
arr.remove (1)
print(arr)

#Удаление элемента по его индексу в массиве
arr = ['a', 'b', 'c', 'd']
del arr[2]
print(arr)