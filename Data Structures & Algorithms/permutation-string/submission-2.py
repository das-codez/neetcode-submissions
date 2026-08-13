class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def index(i):
            return (ord(s2[i]) - ord('a'))
        if len(s2) < len(s1):
            return False
        counts = [0] * 26
        for c in s1:
            counts[ord(c) - ord('a')]+=1
        
        curr = [0] * 26
        for i in range(len(s1)):
            curr[index(i)]+=1
        if curr == counts:
            return True
        i = 0
        for j in range(len(s1), len(s2)):
            curr[index(i)]-=1
            i+=1
            curr[index(j)]+=1
            if curr == counts:
                return True
        return curr == counts
