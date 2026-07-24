class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        for position, speed in cars:

            arrival = (target - position) / speed
            stack.append(arrival)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)