class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(i, curr):
            if i >= len(s):
                ans.append(curr[:])
                return
            for j in range(i, len(s)):
                if check(s[i: j + 1]):
                    curr.append(s[i: j + 1])
                    dfs(j + 1, curr)
                    curr.pop()
        ans = []
        dfs(0, [])
        return ans
        
        