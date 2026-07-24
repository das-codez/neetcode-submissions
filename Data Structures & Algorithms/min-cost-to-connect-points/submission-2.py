class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)
        adj = {i:[] for i in range(v)}
        for i in range(v):
            x1, y1 = points[i]
            for j in range(i + 1, v):
                x2, y2 = points[j]
                cost = abs(x2-x1) + abs(y2-y1)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        
        ans = 0
        q = [[0, 0]]
        seen = set()
        while len(seen) < v:
            cost, u = heapq.heappop(q)
            if u not in seen:
                ans+=cost
                seen.add(u)
                for wei, nei in adj[u]:
                    heapq.heappush(q, [wei, nei])
        return ans