class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        for i in range(len(t)):
            j = 0
            if t[i] == s[j]:
                j+=1
                i+=1
                while j < len(s) and i < len(t):
                    if s[j] == t[i]:
                        j+=1
                    
                    i+=1
                
                if j == len(s): return True
                if i == len(t): return False

        return False