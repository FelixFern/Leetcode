s = "rat"
t = "car"

s_hash = {}
t_hash = {}
if(len(s) != len(t)):
    print(False) 
            
for i in range(len(s)):
    if(s[i] not in s_hash): 
        s_hash[s[i]] = 1
    else:  
        s_hash[s[i]] += 1
    
    if(t[i] not in t_hash): 
        t_hash[t[i]] = 1
    else:  
        t_hash[t[i]] += 1

print(s_hash == t_hash)