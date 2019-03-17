# 1-2
try:
    a = 1 / 0
    print(a)
except:
    print("Exception:ValueError")
finally:
    print("this is the end")

# 3 - no - syntax error - wrong type quotation marks
# try :
#     x = 1
# finally :
#     print(“finally”)

# 4
# 'the excepttions type are: IOError, ImportError, ValueError, KeyboardInterrupt, EOFError'

# 5
# 'the problem is that we will know that there is a exception but not why'

# 6
#    'except IOError - file missing, file not readable, permission on file or folder that make it unrachable
#    'except ZeroDivisionError  - division by zero that is wrong Mathematically'

# 7
my_file = open("C:/Users/chani/OneDrive/Documents/NewFile.txt", 'w', encoding='UTF-8')
my_file.closed
# 8
my_file = open("C:/Users/chani/OneDrive/Documents/NewFile.txt", 'r+', encoding='UTF-8')
my_file.write("elad adi")
my_file.closed

# 9
my_file = open("C:/Users/chani/OneDrive/Documents/NewFile.txt", 'r', encoding='UTF-8')
a = my_file.read()
print(a)
my_file.closed

10  #
my_file = open("C:/Users/chani/OneDrive/Documents/NewFile2.txt", 'w', encoding='utf-8')
my_file.write("היי מה קורה")
my_file.close()

my_file2 = open("C:/Users/chani/OneDrive/Documents/NewFile2.txt", 'r', encoding='utf-8')
a = my_file2.read()
print(a)
my_file2.close()

#challenge
from PIL import Image

filename = "C:/Users/chani/OneDrive/Documents/pil_blue2.png"
img = Image.new('RGB', (180, 70), color='BLUE')
img = img.resize((400,200))
img.save(filename)
