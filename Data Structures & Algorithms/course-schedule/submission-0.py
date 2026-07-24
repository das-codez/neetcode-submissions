class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            reqs[curr].append(pre)
        seen = set()
        def dfs(curr):
            if curr in seen:
                return False
            if reqs[curr] == []:
                return True
            seen.add(curr)
            for pre in reqs[curr]:
                if not dfs(pre):
                    return False
            seen.remove(curr)
            reqs[curr] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True