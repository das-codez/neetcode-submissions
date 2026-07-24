class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal_check(l, r):
            nonlocal ans_len
            nonlocal ans
            while l >= 0 and r < len(s) and s[r] == s[l]:
                new_len = r - l + 1
                if new_len > ans_len:
                    ans_len = new_len
                    ans = s[l:r+1]
                l-=1
                r+=1
        ans = ""
        ans_len = 0
        for i in range(len(s)):
            pal_check(i, i)
            pal_check(i, i + 1)
        return ans
