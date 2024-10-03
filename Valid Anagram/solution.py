def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for character in s:
            count[ord(character)-ord('a')] += 1
        for character in t:
            count[ord(character)-ord('a')] -= 1
        for characterCount in count:
            if characterCount != 0:
                return False
        return True  

# Alternate Solution

def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = Counter(s),Counter(t)
        return countS == countT 