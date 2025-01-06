class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        a = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            a[i] = a[i-1] * nums[i-1]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            a[i] = a[i] * suffix
            suffix = suffix * nums[i]

        
        return a