class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        def find(a):
            curr = a
            while par[curr] != curr:
                par[curr] = par[par[curr]]
                curr = par[curr]
            return curr
        def union(a, b):
            par_a, par_b = find(a), find(b)
            if par_a != par_b:
                par[par_a] = par[par_b]
                return 1
            return 0
        ans = n
        for a, b in edges:
            ans -= union(a, b)
        return ans