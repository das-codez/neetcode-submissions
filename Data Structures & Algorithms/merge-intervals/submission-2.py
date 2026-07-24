class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for interval in intervals:
            stack.append(interval)
            while len(stack) >= 2 and stack[-2][1] >= interval[0]:
                interval = stack.pop()
                old_interval = stack.pop()
                new_interval = [min(old_interval[0], interval[0]), max(old_interval[1], interval[1])]
                stack.append(new_interval)
        return list(stack)
            