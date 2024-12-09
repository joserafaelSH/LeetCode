class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1
        }
        rule1 = {"V", "X"}
        rule2 = {"L", "C"}
        rule3 = {"D", "M"}
        total = 0
        next = None
        for i in range(len(s)-1, -1, -1):
            curr = s[i]

            if not next:
                next = curr
                total+= values[curr]
                continue             

            if next in rule1 and curr == "I":
                total -=1
                next = curr
               

            elif next in rule2 and curr == "X":
                total -=10
                next = curr
                

            elif next in rule3 and curr == "C":
                total -=100
                next = curr
                
            else:
                next = curr
                total+= values[curr]
                
        
        return total

