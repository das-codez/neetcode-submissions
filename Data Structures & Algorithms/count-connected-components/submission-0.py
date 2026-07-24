class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = set()
        def dfs(i, prev):
            if i not in seen:
                seen.add(i)
                for nei in adj[i]:
                    if prev == nei:
                        continue
                    dfs(nei, i)
        ans = 0
        for i in range(n):
            if i not in seen:
                ans+=1
                dfs(i, i-1)
        return ans