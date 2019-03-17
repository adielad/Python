# class Shark:
#     def swim(self):
#         print("the shark is swimming")
#
#     def eat(self):
#         print("the shark is eating")
#
# def main():
#     sammy = Shark()
#     sammy.swim()
#     sammy.eat()
#
# if __name__ == "__main__":
#     main()


##################################################################
#                                                                #
#                  Object access: 1 way                          #
#                                                                #
##################################################################
# class Shark:
#     @staticmethod
#     def swim():
#         print(123)
#
# if __name__ == '__main__':
#     Shark.swim()

##################################################################
#                                                                #
#                  Object access: 2 way                          #
#                                                                #
##################################################################
# class Shark:
#         sharkName = "John"
#
# if __name__ == '__main__':
#     print(Shark.sharkName)
##################################################################
#                                                                #
#                  Constructors                                  #
#                                                                #
##################################################################

# class Shark:
#     def __init__(self, age):
#         self.age = age
#         print(age)
#
# def main():
#     steive = Shark(3)
#
# if __name__ == '__main__':
#     main()
##################################################################
#                                                                #
#                  Inheritance - 1 way                           #
#                                                                #
##################################################################
# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
# class ElectricCar(Car):
#     def __init__(self, model, color, baterry_type):
#         Car.__init__(self, model, color)
#         self.baterry_type = baterry_type
#
# def main():
#     regular_volvo = Car("volvo", "white")
#     electric_volvo =ElectricCar("electronic_volvo", "red", "lithium")
#
# if __name__ == '__main__':
#     main()

##################################################################
#                                                                #
#                  Inheritance - 2 way                           #
#                                                                #
##################################################################
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class ElectricCar(Car):
    def __init__(self, model, color, baterry_type):
        super(ElectricCar, self).__init__(model, color)
        self.baterry_type = baterry_type

def main():
    regular_volvo = Car("volvo", "white")
    electric_volvo =ElectricCar("electronic_volvo", "red", "lithium")
    print(regular_volvo.color)
    print(electric_volvo.model)

if __name__ == '__main__':
    main()


##################################################################
#                                                                #
#                  exemple                          #
#                                                                #
##################################################################
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
