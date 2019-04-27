#A
class  Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# def main():
#     rexi = Dog('rexi', 5)
#     print(rexi.age)
#
# if __name__ == '__main__':
#     main()

#B - it will return 3

# #C
# class Car():
#     @staticmethod
#     def start():
#         print("on")
# if __name__ == '__main__':
#     Car.start()

#D
# class Hasky(Dog):
#     def __init__(self,name,age):
#      super().__init__(name,age)
#
#     def howl(self):
#         print("ohoooo")

# if __name__ == '__main__':
#     dog_jack = Hasky("jack",8)
#     dog_jack.howl()

#E
# class Blackhusky(Hasky):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
#     def return_color(self):
#         return "black"
#
# if __name__ == '__main__':
#     new_black_husky = Blackhusky("jhon",6)
#     new_black_husky.howl()
#     print(new_black_husky.return_color())

#F - it's a static method so we need to add "@staticmethod" and we need to call bark through object of Dog

#G
import array as arr
a = arr.array("i",[ 3,4,5])
for i in a:
    print(i)

a = Dog("jack", 5)
b = Dog("shimon", 7)
c = Dog ("david", 11)
d_list = [a, b, c]
for j in d_list:
    print(j.name)
