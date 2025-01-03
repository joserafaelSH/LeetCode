class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
  
        half = len(nums)//2
        print(nums)
        
        maj = 0
        curr = nums[0]
        maji = 1
        i = 1 

        while i < len(nums): 
            
            if nums[i] != curr:
                if maji > maj:
                    maj = maji
                
                if maj > half:
                    return curr 

                curr = nums[i]
                i+=1
            else:
                maji+=1
                i+=1
        
        return curr
