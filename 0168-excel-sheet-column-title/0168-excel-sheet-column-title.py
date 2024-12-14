class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #0 = A
        #25 = z
        A = 65
        mod = 26
        resp = ""

        while columnNumber > 0 :
            columnNumber -= 1
            resp += chr(columnNumber % mod + A)
            columnNumber //= mod
        
        return resp[::-1]

        