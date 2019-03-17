#1#
print("Hello" +"\n" +"Elad Adi")

#2#
def sumNum(a,b):
    print(a+b)

sumNum(5,4)

#3#
import sys
print(str(sys.version)[:5])

# 4#
def reverse(a):
    b = a[::-1]
    print(b)


reverse("hello")

# 5#
def amount(d):
    e = len(d)
    print(e)


amount("abba")

#6#
import datetime
a = datetime.datetime.now()
print(a)

7#
def bigger(x, y):
    if x>y:
        print(str(x) + " is bigger")
    elif y>x:
        print(str(y) + " is bigger")
    else:
        print("the numbers are equal")

bigger(3, 5)

#8#
def match(a,b,c):
    if a>b and a<c:
        print("MATCH")
    else:
        print("NOT MATCH")


match(100,5,200)