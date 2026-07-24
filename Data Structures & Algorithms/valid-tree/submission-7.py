class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n