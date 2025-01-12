class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = strs[0]
        for i, v  in enumerate(strs):
            if len(v) < len(short):
                short = v 
                strs = strs[0:i] + strs[i+1:]
        
        print(strs, short)
        for i in strs: 
            k = 0
            while k < len(short):
                if i[k] != short[k]:
                    short = short[0:k]
                    if not short:
                        return ""
                
                k+=1
        
        return short
            


        
                
        