class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for inward, out, val in times:
            graph[inward].append((out, val))
        
        q = [(0, k)]
        seen = set()
        t = 0
        while q:
            weight, node = heapq.heappop(q)
            if node in seen:
                continue
            seen.add(node)
            t = weight
            for out, val in graph[node]:
                if out not in seen:
                    heapq.heappush(q, (val + weight, out))
        return t if len(seen) == n else -1