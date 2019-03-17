####################Second class Assiment##########################

# #A#
x = 100
y = 200
if x > y:
    Print("BIG")
else:
    print("Small")

# B#
for i in range(5):
    print(i)

# C#
x = int(input("please enter a number between 1-4 :"))
if x > 0 and x < 5:
    if x == 1:
        print("summer")
    elif x == 2:
        print("winter")
    elif x == 3:
        print("fall")
    else:
        print("spring")
else:
    print("you choose wrong number")

# D#
count = 1
while count < 11:
    print(count)
    count = count + 1

'1. 10 times'
'2. 10'

# E#
Age = 35
FirstLatterOfLastName = 'A'
CurrntDollarShekelCurrency = 3.61
DidYouFlewAbroad = 'True'
AppartmentNumber = 4
CurrencyAge = Age + CurrntDollarShekelCurrency

print(Age)
print(FirstLatterOfLastName)
print(CurrntDollarShekelCurrency)
print(DidYouFlewAbroad)
print(AppartmentNumber)
print(CurrencyAge)

# F#
x = int(input("Please enter your phone number :"))
print("phone number " + str(x))


# G#
def printHello():
    print("hello")


printHello()


#
def calculate():
    a = 5 + 3.2
    print(a)


calculate()


# H#
def name(name):
    print(name)


name('elad')


def divide(num):
    print(num / 2)


divide(12)


# i#
def sum(x, y):
    print(x + y)


sum(3, 4)


def oneWord(a, b):
    print(a + " " + b)


oneWord('elad', 'adi')

# J#
import array as arr

x = arr.array("i", [5, 7, 9])
for a in x:
    print(a)

# K#

for i in range(0, 5):
    for j in range(0, i + 1):
        print("#", end='')
    print("\r")

# L#
for a in range(7):
    for b in range(7):
        if (a == b) or ((7 - b - 1) == a):
            print('*', end='')
        else:
            print(' ', end='')
    print("\r")


# M#
def getNum():
    num = int(input("Please enter a number"))
    return num


def numSum():
    a = str(getNum())
    b = sum([int(i) for i in a])
    print(b)


numSum()
