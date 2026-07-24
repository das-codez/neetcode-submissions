# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node, subNode):
            if not node and not subNode:
                return True
            if node and subNode and node.val == subNode.val:
                return (check(node.left, subNode.left) and check(node.right, subNode.right))
            return False
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            if check(root, subRoot):
                return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))