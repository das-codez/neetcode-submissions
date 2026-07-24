# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, highest):
            if not node:
                return 0
            ans = 1 if node.val >= highest else 0
            new_val = max(node.val, highest)
            ans += helper(node.left, new_val)
            ans += helper(node.right, new_val)
            return ans
        return helper(root, root.val)