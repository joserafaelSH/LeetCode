class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_1 = 0
        pointer_2 = len(s)-1 
 
        while pointer_1 < pointer_2:
            
            while pointer_1 < pointer_2 and not s[pointer_1].isalnum():
                pointer_1 += 1
            
            while pointer_1 < pointer_2 and not s[pointer_2].isalnum():
                pointer_2 -= 1
             
            
            if  s[pointer_1].lower() != s[pointer_2].lower():
                return False 

            pointer_1+=1
            pointer_2-=1

        return True