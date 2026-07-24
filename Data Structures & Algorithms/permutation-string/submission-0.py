class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        counts1 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord('a')] +=1
        counts2 = [0] * 26
        k = len(s1)
        for r in range(len(s2)):
            counts2[ord(s2[r]) - ord('a')] +=1
            if r - l + 1 < k:
                continue
            if counts1 == counts2:
                return True
            counts2[ord(s2[l]) - ord('a')] -=1
            l+=1
        return False