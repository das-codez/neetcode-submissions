# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_indx = in_indx = 0
        def dfs(limit):
            nonlocal pre_indx, in_indx
            if pre_indx >= len(preorder):
                return None
            if inorder[in_indx] == limit:
                in_indx+=1
                return None
            root = TreeNode(preorder[pre_indx])
            pre_indx+=1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))