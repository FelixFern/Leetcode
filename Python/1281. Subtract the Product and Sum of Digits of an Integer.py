n = 234
number = [int(i) for i in str(n)]
product = 1
sums = 0
for i in number:
    product *= i
    sums += i
print(product - sums)