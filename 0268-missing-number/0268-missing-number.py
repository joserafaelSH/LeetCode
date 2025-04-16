class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # [0 ... n]
        
        # Memory is O(1) constant space using the nums
        # O(n)
        def targetExists(nums, target):
            for k in nums:
                if k == target:
                    return True
            return False

        # O(n) * O(n) -> (n^2)
        for i in range(n-1, -1, -1):
            response = targetExists(nums, i)
            if response == False:
                return i

        return n