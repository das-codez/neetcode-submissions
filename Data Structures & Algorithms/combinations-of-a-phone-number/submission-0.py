class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return 
            for j in range(i, len(digits)):
                for c in combos[int(digits[j])]:
                    curr.append(c)
                    backtrack(curr, j+1)
                    curr.pop()
        combos = ["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        backtrack([], 0)
        return ans