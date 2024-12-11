class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0 
        i = len(s) - 1
        while i > -1:
            if s[i] != ' ':
                i -= 1
                count+=1
                while i > -1 and s[i] != ' ':
                    count+=1
                    i -= 1

                return count
            i -=1
        return count 