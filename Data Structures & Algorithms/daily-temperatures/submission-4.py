class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                oldInd = stack[-1][1]
                daysPassed = i - oldInd
                res[oldInd] = daysPassed
                stack.pop()
            stack.append((temp, i))
        return res

