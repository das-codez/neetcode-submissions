# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, highest):
            if not node:
                return 0
            ans = 1 if node.val >= highest else 0
            highest = max(node.val, highest)
            ans += dfs(node.left, highest)
            ans += dfs(node.right, highest)
            return ans

        return dfs(root, root.val)