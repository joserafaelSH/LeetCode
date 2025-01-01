class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # p0 = 0
        # p1 = 0 

        # if len(nums) == 1: return 
        
        # while p0 < len(nums) and p1 < len(nums):
        #     while p0 < len(nums) and nums[p0] != 0:
        #         p0 += 1
            
        #     if p0 == len(nums):
        #         return 
            
        #     while p1 < len(nums) and nums[p1] == 0:
        #         p1 += 1
            
        #     if p1 == len(nums):
        #         return 
            
        #     if p0 < p1:
        #         nums[p0], nums[p1] =  nums[p1], nums[p0]
        #     else:
        #         p1 = p0 + 1

        p0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[p0] =  nums[p0], nums[i]
                p0 += 1
