class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for interval in intervals:
            stack.append(interval)
            if len(stack) >= 2 and stack[-2][1] >= interval[0]:
                stack.pop()
                old_interval = stack.pop()
                new_start = min(old_interval[0], interval[0])
                new_end = max(old_interval[1], interval[1])

                new_interval = [new_start, new_end]
                stack.append(new_interval)
        return list(stack)