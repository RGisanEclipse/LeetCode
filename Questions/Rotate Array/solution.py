def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    temp = [0] * n
    for i in range(n-1, -1, -1):
        temp[n-i-1] = nums[i]
    for i in range(n - k):
        temp[k + i] = nums[i]
    for i in range(k):
        temp[i] = nums[n - k + i]
    for i in range(n):
        nums[i] = temp[i]

# Another solution, but O(n) space

def rotate(self, nums: List[int], k: int) -> None:
    k = k%len(nums)
    nums[:] = nums[-k:] + nums[:-k]