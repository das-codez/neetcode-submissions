class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        distances = [float('inf')] * (n + 1)
        distances[0] = 0
        distances[k] = 0
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            for neigh, weight in graph[node]:
                tot_dist = dist + weight
                if tot_dist < distances[neigh]:
                    distances[neigh] = tot_dist
                    heapq.heappush(heap, (tot_dist, neigh))
        ans = max(distances)
        return ans if ans != float('inf') else -1