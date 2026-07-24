class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        ans = 0
        seen = set()
        heap = [[0, 0]]
        while len(seen) < n:
            cost, i = heapq.heappop(heap)
            if i not in seen:
                ans+=cost
                seen.add(i)
                for neiCost, nei in adj[i]:
                    if nei not in seen:
                        heapq.heappush(heap, [neiCost, nei])
        return ans