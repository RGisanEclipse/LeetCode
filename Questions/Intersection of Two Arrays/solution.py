def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1Elements = set()
    result = []
    for num in nums1:
        nums1Elements.add(num)
    for num in nums2:
        if num in nums1Elements:
            result.append(num)
            nums1Elements.remove(num)
    return result