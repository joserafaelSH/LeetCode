class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zero = 0 
        carry_zero = 0
        for n in nums:
            if n == 0:
                zero+=1 
                zero+= carry_zero
                carry_zero+=1
            else:
                carry_zero = 0 
            
            
    
        return zero