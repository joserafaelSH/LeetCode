class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for k, v in enumerate(nums):
            if v in hash:
                return [k, hash[v]]
            
            aux = target - v
            hash[aux] = k
        
        return []
        
        