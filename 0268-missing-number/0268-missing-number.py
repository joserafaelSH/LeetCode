class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] != 0: return 0 
            else: return n
         
        

        nums.sort() # O(n log(n))
        if nums[0] != 0: return 0
        print(nums)
        for i in range(1, len(nums)): #(O(n))
            if nums[i-1] + 1 != nums[i]:
                return nums[i-1] + 1

        return n