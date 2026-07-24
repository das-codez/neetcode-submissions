class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr, counts, index):
            if tuple(counts) not in seen:
                seen.add(tuple(counts))
                ans.append(curr[:])
                
            
            for i in range(index, len(nums)):
                counts[nums[i] + 20]+=1
                curr.append(nums[i])
                dfs(curr, counts, i + 1)
                curr.pop()
                counts[nums[i] + 20]-=1

        ans = []
        seen = set()
        counts = [0] * 41
        dfs([], counts, 0)
        return ans