x = 20
seen = set()
def count(x) -> int:
    y = [int(i) for i in str(x)]
    n = 0
    for i in y:
        n += i ** 2
    return n 
while count(x) not in seen:
    sum1 = count(x) 
    if sum1 == 1:
        print("True")
        break
    else:
        seen.add(sum1)
        x = sum1
print("False")
        
  
        
