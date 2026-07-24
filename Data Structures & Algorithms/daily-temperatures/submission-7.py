class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temp, index = stack.pop()
                ans[index] = i - index
            stack.append((val, i))
        return ans