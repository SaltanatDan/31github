#Внутри класса могут быть определены атрибуты и методы.
class MyClass:
      attribute = "Some value"
      def my_method(self):
          print("Hello from my_method")

#Чтобы создать объект класса, используйте имя класса со скобками:
my_object = MyClass()

#Для доступа к атрибутам и методам объекта используйте точечную нотацию:
print(my_object.attribute)  # выводит "Some value"
my_object.my_method()  # выводит "Hello from my_method"

class MyClass:
    def __init__(self, attribute_value):
        self.attribute = attribute_value

    def my_method(self):
        print("Hello from my_method")

#При создании объекта класса нужно передать значение для атрибута:
my_object = MyClass("Custom value")
print(my_object.attribute)  # выводит "Custom value"

#Наследование позволяет создать новый класс, который наследует атрибуты и методы родительского класса.
class ParentClass:
    def method1(self):
        print("Method1 of ParentClass")

    def method2(self):
        print("Method2 of ParentClass")


class ChildClass(ParentClass):
    def method3(self):
        print("Method3 of ChildClass")
