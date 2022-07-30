def canConstruct(ransomNote: str, magazine: str) -> bool:
        hash = {}
        hash2 = {}
        
        for i in range(len(ransomNote)):
            if not hash.get(ransomNote[i]):
                hash[ransomNote[i]] = 1 
            else:
                hash[ransomNote[i]] += 1  
        
        for i in range(len(magazine)):
            if not hash2.get(magazine[i]):
                hash2[magazine[i]] = 1 
            else:
                hash2[magazine[i]] += 1  
        
        for key, value in hash.items():
            if key not in hash2:
                return False
            else:
                if hash2.get(key) < value :
                    return False
        
        return True

print(canConstruct("aa", "ab"))