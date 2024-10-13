def findClosestNumber(self, nums: List[int]) -> int:
    biggestNegativeNumber = -sys.maxsize -1
    smallestPositiveNumber = sys.maxsize
    for i in range(len(nums)):
        if nums[i] == 0:
            return 0
        if nums[i] > biggestNegativeNumber and nums[i] < 0:
            biggestNegativeNumber = nums[i]
        elif nums[i] < smallestPositiveNumber and nums[i] > 0:
            smallestPositiveNumber = nums[i]
    if smallestPositiveNumber < (biggestNegativeNumber * -1):
        return smallestPositiveNumber
    elif (biggestNegativeNumber * -1) < smallestPositiveNumber:
        return biggestNegativeNumber
    else:
        return smallestPositiveNumber