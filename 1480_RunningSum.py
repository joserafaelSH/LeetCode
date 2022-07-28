inp = [3,1,2,10,1]

def runningSum(nums):
    memo = [-1 for i in range(len(inp)+1)]
    for i in range(len(inp)):
        if i == 0:
            memo[0] = nums[0]
        else:
            memo[i] = memo[i-1] + nums[i]
    
    print(memo[:-1])


runningSum(inp)