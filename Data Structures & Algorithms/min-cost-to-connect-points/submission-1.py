class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        
        ans = 0
        seen = set()
        heap = [[0,0]]
        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i not in seen:
                ans+=cost
                seen.add(i)
                for new_cost, nei in adj[i]:
                    heapq.heappush(heap, [new_cost, nei])
        return ans

