
def isSubsequence(s: str, t: str): 
    
        lenS = len(s)-1
        lenT = len(t)-1
        if lenS == -1: return True
        if lenT==-1: return False
        
        c = len(s)
        while lenT > -1:
            if lenS == -1:
                break
            if s[lenS] == t[lenT]:
                c-=1 
                lenS-=1 
                lenT-=1 
            else:
                lenT -=1

        return c == 0
        
    


assert(isSubsequence("abc","ahbgdc") == True)
assert(isSubsequence("axc","ahbgdc") == False)
assert(isSubsequence("acb","ahbgdc") == False)
assert(isSubsequence("b","abc") == True)
assert(isSubsequence("","ahbgdc") == True)
assert(isSubsequence("abc","") == False)