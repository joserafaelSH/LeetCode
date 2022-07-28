s = "badc"
t = "baba"

a = "egcd"
b = "adfd"

q = "egg"
w = "add"

r = "foo"
y = "bar"

v = "paper"
c = "title"

def isIsomorphic(s: str, t: str) -> bool:
    hash = {}
    for i in range(len(s)): 
        if s[i] in hash:
            c = hash.get(t[i]) 
            if hash.get(s[i]) != t[i]:
                return False
        else:
            if t[i] in hash.values():
                return False
            else:
                hash[s[i]] = t[i]
    
    return True



assert(isIsomorphic(q,w) == True)
assert(isIsomorphic(r,y) == False)
assert(isIsomorphic(v,c) == True)
assert(isIsomorphic(s,t) == False)
assert(isIsomorphic(a,b) == False)