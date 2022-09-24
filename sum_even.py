number = 2635

counter = 0

x1 = number % 10 + 1
counter += x1 % 2 * (x1 - 1)
number //= 10 

x2 = number % 10 + 1
counter += x2 % 2 * (x2 - 1)
number //= 10 

x3 = number % 10 + 1
counter += x3 % 2 * (x3 - 1)
number //= 10 

x4 = number % 10 + 1
counter += x4 % 2 * (x4 - 1)
number //= 10 

print(counter)