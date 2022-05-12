n = int(input())

def isPowerofThree(x):
    if x == 1:
        return True
    elif x < 1:
        return False
    else: 
        return isPowerofThree(x/3)
print(isPowerofThree(n))