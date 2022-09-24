number = 4579

counter = 0

x1 = number % 10
counter += x1 % 2 * x1
number //= 10 

x2 = number % 10
counter += x2 % 2 * x2
number //= 10 

x3 = number % 10
counter += x3 % 2 * x3
number //= 10 

x4 = number % 10
counter += x4 % 2 * x4
number //= 10 

print(counter)