class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_count = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [key for key, val in sorted_count][:k]