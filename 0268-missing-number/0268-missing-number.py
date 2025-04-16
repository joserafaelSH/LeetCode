class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # [0 ... n]

        def aux(nums, target):
            for k in nums:
                if k == target:
                    return True
            
            return False

        for i in range(n-1, -1, -1):
            response = aux(nums, i)
            if response == False:
                return i

        return n