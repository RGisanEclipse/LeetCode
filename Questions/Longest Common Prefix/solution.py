def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]
    for string in strs:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Alternate solution O(n logn)
def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str1 = strs[0]
        str2 = strs[len(strs)-1]
        counter = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                counter+=1
            else:
                break
        return str1[:counter]