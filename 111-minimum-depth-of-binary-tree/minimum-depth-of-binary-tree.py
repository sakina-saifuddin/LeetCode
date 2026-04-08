# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        node=root

        left=self.minDepth(node.left)
        right=self.minDepth(node.right)

        if node.left is None: #if lef tis not there and right is there with minimum its gonna take 0 as minimum but we want value
            return 1+right
        if node.right is None:
            return 1+left


        return 1+min(left, right)

        