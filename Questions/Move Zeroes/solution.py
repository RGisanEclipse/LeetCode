def moveZeroes(self, nums: List[int]) -> None:
    zeroPointer = 0
    for i in range(0,len(nums)):
        if nums[i] != 0:
            nums[i],nums[zeroPointer] = nums[zeroPointer], nums[i]
            zeroPointer+=1
