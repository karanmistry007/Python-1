tuple1 = (4, 6, 8)
list1 = list(tuple1)
n = int(input("Enter a new value: "))
list1.append(n)
tuple1 = tuple(list1)
print(tuple1)