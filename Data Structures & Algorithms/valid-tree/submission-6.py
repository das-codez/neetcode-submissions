class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set([0])
        q = deque([(0, -1)])

        while q:
            node, parent = q.popleft()
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                q.append((nei, node))
        return len(seen) == n