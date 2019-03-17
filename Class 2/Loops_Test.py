#######################-----for loops------#############
for x in range(5):
    print(x)

for x in range(2, 15):
    print(x)

for x in range(3, 8, 2):
    print(x)

#######################-----while loops------#############
num = 0
while num < 5:
    print(num)
    num += 1

#######################-----break statment------#############
num = 0
while num < 5:
    print(num)
    num += 1
    if num == 3:
        break

#######################-----continue statment------#############
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip num == 3 so we can see that it not print it
    print(num)

#######################-----else in a loop ------#############
