class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = ans = curr = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                curr-=1
                l+=1
            
            seen.add(s[r])
            curr+=1
            
            ans = max(ans, curr)
        return ans
        