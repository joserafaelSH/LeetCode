nums = [1,7,3,6,5,6]

def pivotIndex(nums):

    somaR= 0
    somaL = 0
    for i in range(len(nums)):
        if len(nums) == 1:
            return 0
      
        if i == 0:
            for k in range(i+1,len(nums)):
                
                somaR+=nums[k]
        else:
            somaR-= nums[i]
            somaL += nums[i-1]
            

        if somaR == somaL:
            return i
    
    return -1

    
        

print(pivotIndex(nums))