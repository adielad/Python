import array as arr

a = arr.array("i", [2, 4, 6, 8])
a[0] = 1
#print(a[0])
a.append(11)
#print(a[4])
a.pop(2) # remove an element
a.insert(3, 12) # add 12 to index 3
#print(a[3])

print(len(a))

for x in a:
    print(x)

for i in range(len(a)):
    print(a[i])