class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            reqs[curr].append(pre)
        ans = []
        in_ans, seen = set(), set()
        def dfs(curr):
            if curr in seen:
                return False
            if curr in in_ans:
                return True
            
            seen.add(curr)
            for pre in reqs[curr]:
                if not dfs(pre):
                    return False
            seen.remove(curr)
            in_ans.add(curr)
            ans.append(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans