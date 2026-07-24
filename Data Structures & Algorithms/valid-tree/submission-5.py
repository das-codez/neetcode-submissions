class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            if u == v:
                return False
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        q = deque([0])
        while q:
            node = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    q.append(neighbor)
        return len(seen) == n