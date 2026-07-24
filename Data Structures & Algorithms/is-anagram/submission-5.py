class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1 = [0] * 26
        for c in s:
            char1[ord(c) - ord('a')]+=1
        char2 = [0] * 26
        for c in t:
            char2[ord(c) - ord('a')]+=1
        return char1 == char2