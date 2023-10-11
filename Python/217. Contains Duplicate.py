nums = [1,2,3,1]

hash_map = {}
for i in nums: 
    if(i not in hash_map):
        hash_map[i] = 1
    
    else: 
        print(True)
# using return would solve double print
print(False) 
