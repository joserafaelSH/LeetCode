class Solution:
    def reverseWords(self, s: str) -> str:
        # two pointer aproach 

        left = 0
        right = 0
        whitespace = " "
        inputSize = len(s)
        s = list(s)
        backup = 0
        while left < inputSize or right < inputSize : 
            # find world
            while right < inputSize:
                if s[right] == whitespace:
                    break
                right += 1
            
            
            backup = right
            right-=1
            # reverse current word
            while left <= right-1:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1 
            
            left = backup + 1
            right = left

        return "".join(s)
            