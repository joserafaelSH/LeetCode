class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        pascal = [1,1]
        for i in range(2, rowIndex + 1):
            row = []
            for j in range(i+1):
                curr = 0
                
                if j == 0 or j == i: 
                    curr = 1
                else:
                    curr = pascal[j-1] + pascal[j]
                
                row.append(curr)
            
            pascal = row
        
        return pascal

