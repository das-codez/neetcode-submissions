class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def backtrack(curr, i):
            if i == len(digits):
                ans.append("".join(curr))
                return 
            for c in combos[int(digits[i])]:
                curr.append(c)
                backtrack(curr, i+1)
                curr.pop()
        combos = ["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        backtrack([], 0)
        return ans