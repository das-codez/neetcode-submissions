class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr, total, index):
            if total == target and curr not in ans:
                ans.append(curr[:])
                return
            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                backtrack(curr, total + candidates[i], i + 1)
                curr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans