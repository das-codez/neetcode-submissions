class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(numbers):
            if (target - num) in seen:
                return [seen[target-num], i + 1]
            else:
                seen[num] = i + 1
        return []