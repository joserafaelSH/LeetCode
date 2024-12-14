class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #0 = A
        #25 = z
        A = 65
        mod = 26
        val = 0
        for i in columnTitle:
            val = val * mod + ord(i) + 1 - A
        
        return val