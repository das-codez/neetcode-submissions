class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            distance *= .5
            heapq.heappush(heap,(distance, x, y))
        ans = []
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans