class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for pos, speed in combined:
            curr = (target - pos) / speed
            if stack and stack[-1] < curr:
                stack.append(curr)
            if not stack:
                stack.append(curr)
        return len(stack)