def maxSubArray(self, nums: List[int]) -> int:
    maximumSum = nums[0]
    currentSum = 0
    for i in range(0,len(nums)):
        currentSum += nums[i]
        if currentSum > maximumSum:
            maximumSum = currentSum
        if currentSum < 0:
                currentSum = 0
    return maximumSum