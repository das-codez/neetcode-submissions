class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal_check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len[0]:
                    ans[0] = s[l:r+1]
                    ans_len[0] = r - l + 1
                l-=1
                r+=1
        ans = [""]
        ans_len = [0]
        for i in range(len(s)):
            pal_check(i, i)
            pal_check(i, i + 1)
       
        return ans[0]